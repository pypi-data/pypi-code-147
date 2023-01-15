#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockQuitModel(object):

    def __init__(self):
        self._open_id = None
        self._userid = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.userid:
            if hasattr(self.userid, 'to_alipay_dict'):
                params['userid'] = self.userid.to_alipay_dict()
            else:
                params['userid'] = self.userid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockQuitModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'userid' in d:
            o.userid = d['userid']
        return o


