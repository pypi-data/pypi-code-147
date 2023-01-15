#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SenderInfoVO import SenderInfoVO


class InboundOrder(object):

    def __init__(self):
        self._ext_info = None
        self._inbound_type = None
        self._out_biz_no = None
        self._remark = None
        self._sender_info_vo = None
        self._warehouse_code = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def inbound_type(self):
        return self._inbound_type

    @inbound_type.setter
    def inbound_type(self, value):
        self._inbound_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def sender_info_vo(self):
        return self._sender_info_vo

    @sender_info_vo.setter
    def sender_info_vo(self, value):
        if isinstance(value, SenderInfoVO):
            self._sender_info_vo = value
        else:
            self._sender_info_vo = SenderInfoVO.from_alipay_dict(value)
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.inbound_type:
            if hasattr(self.inbound_type, 'to_alipay_dict'):
                params['inbound_type'] = self.inbound_type.to_alipay_dict()
            else:
                params['inbound_type'] = self.inbound_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sender_info_vo:
            if hasattr(self.sender_info_vo, 'to_alipay_dict'):
                params['sender_info_vo'] = self.sender_info_vo.to_alipay_dict()
            else:
                params['sender_info_vo'] = self.sender_info_vo
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InboundOrder()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'inbound_type' in d:
            o.inbound_type = d['inbound_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'sender_info_vo' in d:
            o.sender_info_vo = d['sender_info_vo']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


