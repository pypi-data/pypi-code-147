#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditUserSystemOauthQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditUserSystemOauthQueryResponse, self).__init__()
        self._access_token = None
        self._expires_in = None
        self._re_expires_in = None
        self._refresh_token = None
        self._user_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value
    @property
    def re_expires_in(self):
        return self._re_expires_in

    @re_expires_in.setter
    def re_expires_in(self, value):
        self._re_expires_in = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditUserSystemOauthQueryResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'expires_in' in response:
            self.expires_in = response['expires_in']
        if 're_expires_in' in response:
            self.re_expires_in = response['re_expires_in']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
        if 'user_id' in response:
            self.user_id = response['user_id']
