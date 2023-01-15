#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityBaseInfo import ActivityBaseInfo
from alipay.aop.api.domain.CustomerGuideModify import CustomerGuideModify
from alipay.aop.api.domain.VoucherAvailableScopeInfo import VoucherAvailableScopeInfo
from alipay.aop.api.domain.VoucherCustomerGuideInfo import VoucherCustomerGuideInfo
from alipay.aop.api.domain.VoucherDisplayInfoModify import VoucherDisplayInfoModify
from alipay.aop.api.domain.VoucherDisplayPatternInfo import VoucherDisplayPatternInfo
from alipay.aop.api.domain.VoucherSendModeInfo import VoucherSendModeInfo
from alipay.aop.api.domain.VoucherSendRuleDetailModify import VoucherSendRuleDetailModify
from alipay.aop.api.domain.VoucherUseRuleModify import VoucherUseRuleModify
from alipay.aop.api.domain.VoucherUseRuleInfo import VoucherUseRuleInfo


class AlipayMarketingActivityOrdervoucherModifyModel(object):

    def __init__(self):
        self._activity_base_info = None
        self._activity_id = None
        self._activity_name = None
        self._customer_guide = None
        self._merchant_access_mode = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._voucher_available_scope_info = None
        self._voucher_available_scope_modify_type = None
        self._voucher_customer_guide_info = None
        self._voucher_display_info = None
        self._voucher_display_pattern_info = None
        self._voucher_send_mode_info = None
        self._voucher_send_rule = None
        self._voucher_use_rule = None
        self._voucher_use_rule_info = None

    @property
    def activity_base_info(self):
        return self._activity_base_info

    @activity_base_info.setter
    def activity_base_info(self, value):
        if isinstance(value, ActivityBaseInfo):
            self._activity_base_info = value
        else:
            self._activity_base_info = ActivityBaseInfo.from_alipay_dict(value)
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def customer_guide(self):
        return self._customer_guide

    @customer_guide.setter
    def customer_guide(self, value):
        if isinstance(value, CustomerGuideModify):
            self._customer_guide = value
        else:
            self._customer_guide = CustomerGuideModify.from_alipay_dict(value)
    @property
    def merchant_access_mode(self):
        return self._merchant_access_mode

    @merchant_access_mode.setter
    def merchant_access_mode(self, value):
        self._merchant_access_mode = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def voucher_available_scope_info(self):
        return self._voucher_available_scope_info

    @voucher_available_scope_info.setter
    def voucher_available_scope_info(self, value):
        if isinstance(value, VoucherAvailableScopeInfo):
            self._voucher_available_scope_info = value
        else:
            self._voucher_available_scope_info = VoucherAvailableScopeInfo.from_alipay_dict(value)
    @property
    def voucher_available_scope_modify_type(self):
        return self._voucher_available_scope_modify_type

    @voucher_available_scope_modify_type.setter
    def voucher_available_scope_modify_type(self, value):
        self._voucher_available_scope_modify_type = value
    @property
    def voucher_customer_guide_info(self):
        return self._voucher_customer_guide_info

    @voucher_customer_guide_info.setter
    def voucher_customer_guide_info(self, value):
        if isinstance(value, VoucherCustomerGuideInfo):
            self._voucher_customer_guide_info = value
        else:
            self._voucher_customer_guide_info = VoucherCustomerGuideInfo.from_alipay_dict(value)
    @property
    def voucher_display_info(self):
        return self._voucher_display_info

    @voucher_display_info.setter
    def voucher_display_info(self, value):
        if isinstance(value, VoucherDisplayInfoModify):
            self._voucher_display_info = value
        else:
            self._voucher_display_info = VoucherDisplayInfoModify.from_alipay_dict(value)
    @property
    def voucher_display_pattern_info(self):
        return self._voucher_display_pattern_info

    @voucher_display_pattern_info.setter
    def voucher_display_pattern_info(self, value):
        if isinstance(value, VoucherDisplayPatternInfo):
            self._voucher_display_pattern_info = value
        else:
            self._voucher_display_pattern_info = VoucherDisplayPatternInfo.from_alipay_dict(value)
    @property
    def voucher_send_mode_info(self):
        return self._voucher_send_mode_info

    @voucher_send_mode_info.setter
    def voucher_send_mode_info(self, value):
        if isinstance(value, VoucherSendModeInfo):
            self._voucher_send_mode_info = value
        else:
            self._voucher_send_mode_info = VoucherSendModeInfo.from_alipay_dict(value)
    @property
    def voucher_send_rule(self):
        return self._voucher_send_rule

    @voucher_send_rule.setter
    def voucher_send_rule(self, value):
        if isinstance(value, VoucherSendRuleDetailModify):
            self._voucher_send_rule = value
        else:
            self._voucher_send_rule = VoucherSendRuleDetailModify.from_alipay_dict(value)
    @property
    def voucher_use_rule(self):
        return self._voucher_use_rule

    @voucher_use_rule.setter
    def voucher_use_rule(self, value):
        if isinstance(value, VoucherUseRuleModify):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = VoucherUseRuleModify.from_alipay_dict(value)
    @property
    def voucher_use_rule_info(self):
        return self._voucher_use_rule_info

    @voucher_use_rule_info.setter
    def voucher_use_rule_info(self, value):
        if isinstance(value, VoucherUseRuleInfo):
            self._voucher_use_rule_info = value
        else:
            self._voucher_use_rule_info = VoucherUseRuleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_base_info:
            if hasattr(self.activity_base_info, 'to_alipay_dict'):
                params['activity_base_info'] = self.activity_base_info.to_alipay_dict()
            else:
                params['activity_base_info'] = self.activity_base_info
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.customer_guide:
            if hasattr(self.customer_guide, 'to_alipay_dict'):
                params['customer_guide'] = self.customer_guide.to_alipay_dict()
            else:
                params['customer_guide'] = self.customer_guide
        if self.merchant_access_mode:
            if hasattr(self.merchant_access_mode, 'to_alipay_dict'):
                params['merchant_access_mode'] = self.merchant_access_mode.to_alipay_dict()
            else:
                params['merchant_access_mode'] = self.merchant_access_mode
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.publish_start_time:
            if hasattr(self.publish_start_time, 'to_alipay_dict'):
                params['publish_start_time'] = self.publish_start_time.to_alipay_dict()
            else:
                params['publish_start_time'] = self.publish_start_time
        if self.voucher_available_scope_info:
            if hasattr(self.voucher_available_scope_info, 'to_alipay_dict'):
                params['voucher_available_scope_info'] = self.voucher_available_scope_info.to_alipay_dict()
            else:
                params['voucher_available_scope_info'] = self.voucher_available_scope_info
        if self.voucher_available_scope_modify_type:
            if hasattr(self.voucher_available_scope_modify_type, 'to_alipay_dict'):
                params['voucher_available_scope_modify_type'] = self.voucher_available_scope_modify_type.to_alipay_dict()
            else:
                params['voucher_available_scope_modify_type'] = self.voucher_available_scope_modify_type
        if self.voucher_customer_guide_info:
            if hasattr(self.voucher_customer_guide_info, 'to_alipay_dict'):
                params['voucher_customer_guide_info'] = self.voucher_customer_guide_info.to_alipay_dict()
            else:
                params['voucher_customer_guide_info'] = self.voucher_customer_guide_info
        if self.voucher_display_info:
            if hasattr(self.voucher_display_info, 'to_alipay_dict'):
                params['voucher_display_info'] = self.voucher_display_info.to_alipay_dict()
            else:
                params['voucher_display_info'] = self.voucher_display_info
        if self.voucher_display_pattern_info:
            if hasattr(self.voucher_display_pattern_info, 'to_alipay_dict'):
                params['voucher_display_pattern_info'] = self.voucher_display_pattern_info.to_alipay_dict()
            else:
                params['voucher_display_pattern_info'] = self.voucher_display_pattern_info
        if self.voucher_send_mode_info:
            if hasattr(self.voucher_send_mode_info, 'to_alipay_dict'):
                params['voucher_send_mode_info'] = self.voucher_send_mode_info.to_alipay_dict()
            else:
                params['voucher_send_mode_info'] = self.voucher_send_mode_info
        if self.voucher_send_rule:
            if hasattr(self.voucher_send_rule, 'to_alipay_dict'):
                params['voucher_send_rule'] = self.voucher_send_rule.to_alipay_dict()
            else:
                params['voucher_send_rule'] = self.voucher_send_rule
        if self.voucher_use_rule:
            if hasattr(self.voucher_use_rule, 'to_alipay_dict'):
                params['voucher_use_rule'] = self.voucher_use_rule.to_alipay_dict()
            else:
                params['voucher_use_rule'] = self.voucher_use_rule
        if self.voucher_use_rule_info:
            if hasattr(self.voucher_use_rule_info, 'to_alipay_dict'):
                params['voucher_use_rule_info'] = self.voucher_use_rule_info.to_alipay_dict()
            else:
                params['voucher_use_rule_info'] = self.voucher_use_rule_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityOrdervoucherModifyModel()
        if 'activity_base_info' in d:
            o.activity_base_info = d['activity_base_info']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'customer_guide' in d:
            o.customer_guide = d['customer_guide']
        if 'merchant_access_mode' in d:
            o.merchant_access_mode = d['merchant_access_mode']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'voucher_available_scope_info' in d:
            o.voucher_available_scope_info = d['voucher_available_scope_info']
        if 'voucher_available_scope_modify_type' in d:
            o.voucher_available_scope_modify_type = d['voucher_available_scope_modify_type']
        if 'voucher_customer_guide_info' in d:
            o.voucher_customer_guide_info = d['voucher_customer_guide_info']
        if 'voucher_display_info' in d:
            o.voucher_display_info = d['voucher_display_info']
        if 'voucher_display_pattern_info' in d:
            o.voucher_display_pattern_info = d['voucher_display_pattern_info']
        if 'voucher_send_mode_info' in d:
            o.voucher_send_mode_info = d['voucher_send_mode_info']
        if 'voucher_send_rule' in d:
            o.voucher_send_rule = d['voucher_send_rule']
        if 'voucher_use_rule' in d:
            o.voucher_use_rule = d['voucher_use_rule']
        if 'voucher_use_rule_info' in d:
            o.voucher_use_rule_info = d['voucher_use_rule_info']
        return o


