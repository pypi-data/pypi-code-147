#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthCommoditySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthCommoditySyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthCommoditySyncResponse, self).parse_response_content(response_content)
