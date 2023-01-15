#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CampusInfo import CampusInfo


class SchoolBaseInfo(object):

    def __init__(self):
        self._campus_info = None
        self._city_code = None
        self._inst_id = None
        self._inst_name = None
        self._inst_std_code = None
        self._province_code = None

    @property
    def campus_info(self):
        return self._campus_info

    @campus_info.setter
    def campus_info(self, value):
        if isinstance(value, list):
            self._campus_info = list()
            for i in value:
                if isinstance(i, CampusInfo):
                    self._campus_info.append(i)
                else:
                    self._campus_info.append(CampusInfo.from_alipay_dict(i))
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def inst_std_code(self):
        return self._inst_std_code

    @inst_std_code.setter
    def inst_std_code(self, value):
        self._inst_std_code = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_info:
            if isinstance(self.campus_info, list):
                for i in range(0, len(self.campus_info)):
                    element = self.campus_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.campus_info[i] = element.to_alipay_dict()
            if hasattr(self.campus_info, 'to_alipay_dict'):
                params['campus_info'] = self.campus_info.to_alipay_dict()
            else:
                params['campus_info'] = self.campus_info
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.inst_std_code:
            if hasattr(self.inst_std_code, 'to_alipay_dict'):
                params['inst_std_code'] = self.inst_std_code.to_alipay_dict()
            else:
                params['inst_std_code'] = self.inst_std_code
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SchoolBaseInfo()
        if 'campus_info' in d:
            o.campus_info = d['campus_info']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'inst_std_code' in d:
            o.inst_std_code = d['inst_std_code']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o


