#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmountWf import AmountWf


class MybankCreditSupplychainWfSettlementofexchangeQueryModel(object):

    def __init__(self):
        self._exchangeamount = None
        self._requestid = None
        self._scene = None
        self._sellerid = None
        self._site = None
        self._siteuserid = None

    @property
    def exchangeamount(self):
        return self._exchangeamount

    @exchangeamount.setter
    def exchangeamount(self, value):
        if isinstance(value, AmountWf):
            self._exchangeamount = value
        else:
            self._exchangeamount = AmountWf.from_alipay_dict(value)
    @property
    def requestid(self):
        return self._requestid

    @requestid.setter
    def requestid(self, value):
        self._requestid = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sellerid(self):
        return self._sellerid

    @sellerid.setter
    def sellerid(self, value):
        self._sellerid = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def siteuserid(self):
        return self._siteuserid

    @siteuserid.setter
    def siteuserid(self, value):
        self._siteuserid = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchangeamount:
            if hasattr(self.exchangeamount, 'to_alipay_dict'):
                params['exchangeamount'] = self.exchangeamount.to_alipay_dict()
            else:
                params['exchangeamount'] = self.exchangeamount
        if self.requestid:
            if hasattr(self.requestid, 'to_alipay_dict'):
                params['requestid'] = self.requestid.to_alipay_dict()
            else:
                params['requestid'] = self.requestid
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sellerid:
            if hasattr(self.sellerid, 'to_alipay_dict'):
                params['sellerid'] = self.sellerid.to_alipay_dict()
            else:
                params['sellerid'] = self.sellerid
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.siteuserid:
            if hasattr(self.siteuserid, 'to_alipay_dict'):
                params['siteuserid'] = self.siteuserid.to_alipay_dict()
            else:
                params['siteuserid'] = self.siteuserid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainWfSettlementofexchangeQueryModel()
        if 'exchangeamount' in d:
            o.exchangeamount = d['exchangeamount']
        if 'requestid' in d:
            o.requestid = d['requestid']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sellerid' in d:
            o.sellerid = d['sellerid']
        if 'site' in d:
            o.site = d['site']
        if 'siteuserid' in d:
            o.siteuserid = d['siteuserid']
        return o


