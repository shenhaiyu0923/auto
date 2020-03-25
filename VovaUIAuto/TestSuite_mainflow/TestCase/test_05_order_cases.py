#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Public.ReadConfig import ReadConfig
from PageObject import third_pay, user_center, search, order_details, my_orders, payment
from Public import BaseSteps
from Public.Decorator import *
from Public.Test_data import get_test_data


# @unittest.skip
class TestOrders(unittest.TestCase, BasePage):
    '''订单相关测试'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_clear('com.vova.android')
        cls.d.app_start("com.vova.android")
        cls.test_data = get_test_data(cls.d)
        cls.watch_device("Pretty Sure|GET IT!|总是允许|Baik, saya paham.")
        BaseSteps.init_app_operation()
        cls.test_env = ReadConfig().get_test_env()

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.unwatch_device()

    @setup
    def setUp(self):
        self.d.app_start("com.vova.android")

    @teardown
    def tearDown(self):
        self.d.app_stop("com.vova.android")

    # @unittest.skip
    @testcase
    def test_01_transfer_order(self):
        '''订单转移'''
        BaseSteps.search_goods_by_id(self.test_data['normal_goods_id'])
        BaseSteps.buy_goods_with_attr(self.test_data['normal_goods_attr'])
        BaseSteps.checkout_without_coupon()

        BaseSteps.ensure_needed_country_and_address('Indonesia')
        BaseSteps.checkout_to_change_payment_method('Credit')
        self.press_back_until_special_element(
            self.d(resourceId="com.vova.android:id/order_support_type", text='OTHER DETAILS'),
            timeout=5
        )
        order_details.order_details_page().wait_page()
        a = order_details.order_details_page().get_order_id()
        log.i('待转移的订单号:%s' % a)
        BasePage().press_back_to_home()
        BaseSteps.user_login(self.test_data['user_name_02'], self.test_data['password_02'])
        user_center.user_page().click_my_orders_button()
        my_orders.my_orders_page().wait_page()
        my_orders.my_orders_page().click_unpaid_button()
        order_details.order_details_page().wait_page()
        b = order_details.order_details_page().get_order_id()
        log.i('订单转移账户最新订单号:%s' % b)
        self.assertEqual(a, b, '待转移的订单号和订单转移账户最新订单号不一致，疑订单转移有误')

    # @unittest.skip
    @testcase
    def test_02_change_pay_method_and_address_repay(self):
        '''未支付订单-切换地址和支付方式后重新支付'''
        # BaseSteps.init_app_operation()
        # BaseSteps.user_login(self.test_data['user_name_02'], self.test_data['password_02'])
        BaseSteps.one_step_to_pay(
            'Indonesia', self.test_data['normal_goods_id'],
            self.test_data['normal_goods_attr'], 'Bank Transfers', index=0)
        payment.payment_page().click_confirm_to_pay()

        # change p_method and address retry
        third_pay.third_pay_page().wait_web_page()
        self.press_back_until_special_element(
            self.d(resourceId="com.vova.android:id/order_support_type", text='OTHER DETAILS'),
            timeout=10
        )
        order_details.order_details_page().wait_page()
        BaseSteps.order_detail_change_address('hjzhudejia')
        self.assertTrue(self.d(
            resourceId="com.vova.android:id/address_tv", textContains='hjzhu').exists(timeout=5))

        BaseSteps.order_detail_change_address('vovadejia')
        self.d(resourceId="com.vova.android:id/address_tv", textContains='hjzhu').wait_gone(timeout=4.0)
        self.assertFalse(self.d(
            resourceId="com.vova.android:id/address_tv", textContains='hjzhu').exists(timeout=5))

        BaseSteps.order_detail_to_change_payment_method('OVO CASH')
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(text="GO BACK"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="invoice-pending-left-content"))
