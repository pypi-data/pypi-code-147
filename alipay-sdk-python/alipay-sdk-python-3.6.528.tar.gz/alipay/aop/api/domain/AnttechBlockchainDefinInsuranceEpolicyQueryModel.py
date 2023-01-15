#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinInsuranceEpolicyQueryModel(object):

    def __init__(self):
        self._apply_trade_no = None
        self._business_code = None
        self._platform_access_type = None
        self._platform_code = None
        self._policy_no = None
        self._product_code = None
        self._trade_no = None

    @property
    def apply_trade_no(self):
        return self._apply_trade_no

    @apply_trade_no.setter
    def apply_trade_no(self, value):
        self._apply_trade_no = value
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def platform_access_type(self):
        return self._platform_access_type

    @platform_access_type.setter
    def platform_access_type(self, value):
        self._platform_access_type = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_trade_no:
            if hasattr(self.apply_trade_no, 'to_alipay_dict'):
                params['apply_trade_no'] = self.apply_trade_no.to_alipay_dict()
            else:
                params['apply_trade_no'] = self.apply_trade_no
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.platform_access_type:
            if hasattr(self.platform_access_type, 'to_alipay_dict'):
                params['platform_access_type'] = self.platform_access_type.to_alipay_dict()
            else:
                params['platform_access_type'] = self.platform_access_type
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinInsuranceEpolicyQueryModel()
        if 'apply_trade_no' in d:
            o.apply_trade_no = d['apply_trade_no']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'platform_access_type' in d:
            o.platform_access_type = d['platform_access_type']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


