#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataInquiryorderUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataInquiryorderUploadResponse, self).__init__()
        self._error_message = None
        self._order_id = None
        self._result_code = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataInquiryorderUploadResponse, self).parse_response_content(response_content)
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
