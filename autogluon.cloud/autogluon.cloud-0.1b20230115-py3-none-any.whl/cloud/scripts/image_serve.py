# flake8: noqa
import base64
import hashlib
import os
from io import BytesIO

import numpy as np
import pandas as pd
from PIL import Image

from autogluon.core.constants import QUANTILE, REGRESSION
from autogluon.core.utils import get_pred_from_proba_df
from autogluon.vision import ImagePredictor

image_dir = os.path.join("/tmp", "ag_images")


def _save_images(im, im_name):
    os.makedirs(image_dir, exist_ok=True)
    im_path = os.path.join(image_dir, im_name)
    im.save(im_path)

    return im_path


def model_fn(model_dir):
    """loads model from previously saved artifact"""
    model = ImagePredictor.load(model_dir)

    return model


def transform_fn(model, request_body, input_content_type, output_content_type="application/json"):

    if input_content_type == "application/x-npy":
        buf = BytesIO(request_body)
        data = np.load(buf, allow_pickle=True)
        image_paths = []
        for bytes in data:
            im_bytes = base64.b85decode(bytes)
            # nosec B303 - not a cryptographic use
            im_hash = hashlib.sha1(im_bytes).hexdigest()
            im_name = f"image_{im_hash}.png"
            im = Image.open(BytesIO(im_bytes))
            im_path = _save_images(im, im_name)
            image_paths.append(im_path)

    elif input_content_type == "application/x-image":
        buf = BytesIO(request_body)
        im = Image.open(buf)
        image_paths = []
        im_name = "test.png"
        im_path = _save_images(im, im_name)
        image_paths.append(im_path)

    else:
        raise ValueError(f"{input_content_type} input content type not supported.")

    if model._problem_type not in [REGRESSION, QUANTILE]:
        pred_proba = model.predict_proba(image_paths, as_pandas=True)
        pred = get_pred_from_proba_df(pred_proba, problem_type=model._problem_type)
        pred_proba.columns = [str(c) + "_proba" for c in pred_proba.columns]
        pred.name = "label"  # ImagePredictor doesn't have `label` attribute. Use "label" for now
        prediction = pd.concat([pred, pred_proba], axis=1)
    else:
        prediction = model.predict(image_paths, as_pandas=True)
    if isinstance(prediction, pd.Series):
        prediction = prediction.to_frame()

    if "application/x-parquet" in output_content_type:
        prediction.columns = prediction.columns.astype(str)
        output = prediction.to_parquet()
        output_content_type = "application/x-parquet"
    elif "application/json" in output_content_type:
        output = prediction.to_json()
        output_content_type = "application/json"
    elif "text/csv" in output_content_type:
        output = prediction.to_csv(index=None)
        output_content_type = "text/csv"
    else:
        raise ValueError(f"{output_content_type} content type not supported")

    return output, output_content_type
