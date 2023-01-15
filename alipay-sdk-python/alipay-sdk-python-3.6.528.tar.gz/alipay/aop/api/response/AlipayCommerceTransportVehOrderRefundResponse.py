#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportVehOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehOrderRefundResponse, self).__init__()
        self._refund_amount = None
        self._refund_applets_service_amount = None
        self._trade_no = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_applets_service_amount(self):
        return self._refund_applets_service_amount

    @refund_applets_service_amount.setter
    def refund_applets_service_amount(self, value):
        self._refund_applets_service_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehOrderRefundResponse, self).parse_response_content(response_content)
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_applets_service_amount' in response:
            self.refund_applets_service_amount = response['refund_applets_service_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
