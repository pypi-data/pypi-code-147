#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportParkingEnterinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportParkingEnterinfoSyncResponse, self).__init__()
        self._agreement_scene = None
        self._biz_code = None
        self._biz_msg = None

    @property
    def agreement_scene(self):
        return self._agreement_scene

    @agreement_scene.setter
    def agreement_scene(self, value):
        self._agreement_scene = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportParkingEnterinfoSyncResponse, self).parse_response_content(response_content)
        if 'agreement_scene' in response:
            self.agreement_scene = response['agreement_scene']
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
