#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerCansearchModifyModel(object):

    def __init__(self):
        self._app_origin = None
        self._can_search = None
        self._dev_id = None
        self._mini_app_id = None
        self._operate_id = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def can_search(self):
        return self._can_search

    @can_search.setter
    def can_search(self, value):
        self._can_search = value
    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def operate_id(self):
        return self._operate_id

    @operate_id.setter
    def operate_id(self, value):
        self._operate_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.can_search:
            if hasattr(self.can_search, 'to_alipay_dict'):
                params['can_search'] = self.can_search.to_alipay_dict()
            else:
                params['can_search'] = self.can_search
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.operate_id:
            if hasattr(self.operate_id, 'to_alipay_dict'):
                params['operate_id'] = self.operate_id.to_alipay_dict()
            else:
                params['operate_id'] = self.operate_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerCansearchModifyModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'can_search' in d:
            o.can_search = d['can_search']
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'operate_id' in d:
            o.operate_id = d['operate_id']
        return o


