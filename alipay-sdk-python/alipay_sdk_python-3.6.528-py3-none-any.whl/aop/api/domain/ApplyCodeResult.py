#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CodeResult import CodeResult


class ApplyCodeResult(object):

    def __init__(self):
        self._biz_id = None
        self._code_result = None
        self._error_code = None
        self._error_message = None
        self._success = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def code_result(self):
        return self._code_result

    @code_result.setter
    def code_result(self, value):
        if isinstance(value, CodeResult):
            self._code_result = value
        else:
            self._code_result = CodeResult.from_alipay_dict(value)
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.code_result:
            if hasattr(self.code_result, 'to_alipay_dict'):
                params['code_result'] = self.code_result.to_alipay_dict()
            else:
                params['code_result'] = self.code_result
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyCodeResult()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'code_result' in d:
            o.code_result = d['code_result']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'success' in d:
            o.success = d['success']
        return o


