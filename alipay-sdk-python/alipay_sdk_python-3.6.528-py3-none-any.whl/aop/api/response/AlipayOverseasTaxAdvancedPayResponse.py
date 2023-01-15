#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTaxAdvancedPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTaxAdvancedPayResponse, self).__init__()
        self._out_request_no = None
        self._tax_refund_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def tax_refund_no(self):
        return self._tax_refund_no

    @tax_refund_no.setter
    def tax_refund_no(self, value):
        self._tax_refund_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTaxAdvancedPayResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'tax_refund_no' in response:
            self.tax_refund_no = response['tax_refund_no']
