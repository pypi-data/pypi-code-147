#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityBaseInfo import ActivityBaseInfo
from alipay.aop.api.domain.PaymentVoucherBelongMerchantInfo import PaymentVoucherBelongMerchantInfo
from alipay.aop.api.domain.VoucherSummary import VoucherSummary
from alipay.aop.api.domain.VoucherAvailableScopeInfo import VoucherAvailableScopeInfo
from alipay.aop.api.domain.PaymentVoucherBudgetInfo import PaymentVoucherBudgetInfo
from alipay.aop.api.domain.VoucherBudgetSupplyInfo import VoucherBudgetSupplyInfo
from alipay.aop.api.domain.VoucherCustomerGuideInfo import VoucherCustomerGuideInfo
from alipay.aop.api.domain.VoucherDeductInfo import VoucherDeductInfo
from alipay.aop.api.domain.PaymentVoucherDisplayInfo import PaymentVoucherDisplayInfo
from alipay.aop.api.domain.VoucherDisplayPatternInfo import VoucherDisplayPatternInfo
from alipay.aop.api.domain.VoucherInventoryInfo import VoucherInventoryInfo
from alipay.aop.api.domain.VoucherSendModeInfo import VoucherSendModeInfo
from alipay.aop.api.domain.PaymentVoucherSendRule import PaymentVoucherSendRule
from alipay.aop.api.domain.PaymentVoucherUseRuleDetail import PaymentVoucherUseRuleDetail
from alipay.aop.api.domain.VoucherUseRuleInfo import VoucherUseRuleInfo


class AlipayMarketingActivityVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityVoucherQueryResponse, self).__init__()
        self._activity_base_info = None
        self._activity_id = None
        self._activity_name = None
        self._activity_status = None
        self._belong_merchant_info = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._summary = None
        self._voucher_available_scope_info = None
        self._voucher_budget_info = None
        self._voucher_budget_supply_info = None
        self._voucher_customer_guide_info = None
        self._voucher_deduct_info = None
        self._voucher_display_info = None
        self._voucher_display_pattern_info = None
        self._voucher_inventory_info = None
        self._voucher_send_mode_info = None
        self._voucher_send_rule = None
        self._voucher_type = None
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
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, PaymentVoucherBelongMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = PaymentVoucherBelongMerchantInfo.from_alipay_dict(value)
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
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if isinstance(value, VoucherSummary):
            self._summary = value
        else:
            self._summary = VoucherSummary.from_alipay_dict(value)
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
    def voucher_budget_info(self):
        return self._voucher_budget_info

    @voucher_budget_info.setter
    def voucher_budget_info(self, value):
        if isinstance(value, PaymentVoucherBudgetInfo):
            self._voucher_budget_info = value
        else:
            self._voucher_budget_info = PaymentVoucherBudgetInfo.from_alipay_dict(value)
    @property
    def voucher_budget_supply_info(self):
        return self._voucher_budget_supply_info

    @voucher_budget_supply_info.setter
    def voucher_budget_supply_info(self, value):
        if isinstance(value, VoucherBudgetSupplyInfo):
            self._voucher_budget_supply_info = value
        else:
            self._voucher_budget_supply_info = VoucherBudgetSupplyInfo.from_alipay_dict(value)
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
    def voucher_deduct_info(self):
        return self._voucher_deduct_info

    @voucher_deduct_info.setter
    def voucher_deduct_info(self, value):
        if isinstance(value, VoucherDeductInfo):
            self._voucher_deduct_info = value
        else:
            self._voucher_deduct_info = VoucherDeductInfo.from_alipay_dict(value)
    @property
    def voucher_display_info(self):
        return self._voucher_display_info

    @voucher_display_info.setter
    def voucher_display_info(self, value):
        if isinstance(value, PaymentVoucherDisplayInfo):
            self._voucher_display_info = value
        else:
            self._voucher_display_info = PaymentVoucherDisplayInfo.from_alipay_dict(value)
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
    def voucher_inventory_info(self):
        return self._voucher_inventory_info

    @voucher_inventory_info.setter
    def voucher_inventory_info(self, value):
        if isinstance(value, VoucherInventoryInfo):
            self._voucher_inventory_info = value
        else:
            self._voucher_inventory_info = VoucherInventoryInfo.from_alipay_dict(value)
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
        if isinstance(value, PaymentVoucherSendRule):
            self._voucher_send_rule = value
        else:
            self._voucher_send_rule = PaymentVoucherSendRule.from_alipay_dict(value)
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_use_rule(self):
        return self._voucher_use_rule

    @voucher_use_rule.setter
    def voucher_use_rule(self, value):
        if isinstance(value, PaymentVoucherUseRuleDetail):
            self._voucher_use_rule = value
        else:
            self._voucher_use_rule = PaymentVoucherUseRuleDetail.from_alipay_dict(value)
    @property
    def voucher_use_rule_info(self):
        return self._voucher_use_rule_info

    @voucher_use_rule_info.setter
    def voucher_use_rule_info(self, value):
        if isinstance(value, VoucherUseRuleInfo):
            self._voucher_use_rule_info = value
        else:
            self._voucher_use_rule_info = VoucherUseRuleInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityVoucherQueryResponse, self).parse_response_content(response_content)
        if 'activity_base_info' in response:
            self.activity_base_info = response['activity_base_info']
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'belong_merchant_info' in response:
            self.belong_merchant_info = response['belong_merchant_info']
        if 'publish_end_time' in response:
            self.publish_end_time = response['publish_end_time']
        if 'publish_start_time' in response:
            self.publish_start_time = response['publish_start_time']
        if 'summary' in response:
            self.summary = response['summary']
        if 'voucher_available_scope_info' in response:
            self.voucher_available_scope_info = response['voucher_available_scope_info']
        if 'voucher_budget_info' in response:
            self.voucher_budget_info = response['voucher_budget_info']
        if 'voucher_budget_supply_info' in response:
            self.voucher_budget_supply_info = response['voucher_budget_supply_info']
        if 'voucher_customer_guide_info' in response:
            self.voucher_customer_guide_info = response['voucher_customer_guide_info']
        if 'voucher_deduct_info' in response:
            self.voucher_deduct_info = response['voucher_deduct_info']
        if 'voucher_display_info' in response:
            self.voucher_display_info = response['voucher_display_info']
        if 'voucher_display_pattern_info' in response:
            self.voucher_display_pattern_info = response['voucher_display_pattern_info']
        if 'voucher_inventory_info' in response:
            self.voucher_inventory_info = response['voucher_inventory_info']
        if 'voucher_send_mode_info' in response:
            self.voucher_send_mode_info = response['voucher_send_mode_info']
        if 'voucher_send_rule' in response:
            self.voucher_send_rule = response['voucher_send_rule']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
        if 'voucher_use_rule' in response:
            self.voucher_use_rule = response['voucher_use_rule']
        if 'voucher_use_rule_info' in response:
            self.voucher_use_rule_info = response['voucher_use_rule_info']
