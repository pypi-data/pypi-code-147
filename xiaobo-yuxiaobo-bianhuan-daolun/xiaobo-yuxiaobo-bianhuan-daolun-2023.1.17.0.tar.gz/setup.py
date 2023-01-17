#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import XiaoboYuxiaoboBianhuanDaolun
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('XiaoboYuxiaoboBianhuanDaolun'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="xiaobo-yuxiaobo-bianhuan-daolun",
    version=XiaoboYuxiaoboBianhuanDaolun.__version__,
    url="https://github.com/apachecn/xiaobo-yuxiaobo-bianhuan-daolun",
    author=XiaoboYuxiaoboBianhuanDaolun.__author__,
    author_email=XiaoboYuxiaoboBianhuanDaolun.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="35-小波与小波变换导论",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "xiaobo-yuxiaobo-bianhuan-daolun=XiaoboYuxiaoboBianhuanDaolun.__main__:main",
            "XiaoboYuxiaoboBianhuanDaolun=XiaoboYuxiaoboBianhuanDaolun.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
