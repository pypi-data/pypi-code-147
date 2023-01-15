#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiItemModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemModifyResponse, self).__init__()
        self._item_id = None
        self._request_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiItemModifyResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'request_id' in response:
            self.request_id = response['request_id']
