#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeOverdraftReturnmoneyModel(object):

    def __init__(self):
        self._out_request_no = None
        self._out_trade_no = None
        self._refund_out_request_no = None
        self._trade_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_out_request_no(self):
        return self._refund_out_request_no

    @refund_out_request_no.setter
    def refund_out_request_no(self, value):
        self._refund_out_request_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.refund_out_request_no:
            if hasattr(self.refund_out_request_no, 'to_alipay_dict'):
                params['refund_out_request_no'] = self.refund_out_request_no.to_alipay_dict()
            else:
                params['refund_out_request_no'] = self.refund_out_request_no
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
        o = AlipayTradeOverdraftReturnmoneyModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'refund_out_request_no' in d:
            o.refund_out_request_no = d['refund_out_request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


