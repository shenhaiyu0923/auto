#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Public.ReadConfig import ReadConfig
from PageObject import login, bag, payment, add_a_card, shipping_address, checkout_v2, add_address_v2, order_details
from Public.Decorator import *
from Public.Test_data import get_test_data
from Public import BaseSteps


# @unittest.skip
class TestSpecialPay(unittest.TestCase, BasePage):
    '''支付中特殊操作测试'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_clear('com.vova.android')
        cls.d.app_start("com.vova.android")
        # 无注册case别在watch中增加Shop Now，否则购物车为空时，会默认点击，返回上个页面在加车成功之前
        cls.watch_device("Pretty Sure|Sure|Baik, saya paham.|GET IT!|总是允许|始终允许")
        cls.test_data = get_test_data(cls.d)
        cls.test_env = ReadConfig().get_test_env()
        BaseSteps.init_app_operation()
        BaseSteps.user_login(cls.test_data['user_name_02'], cls.test_data['password_02'])
        cls.PAN = "EHFGA5967A"
        cls.CPF = '12649239700'

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
    def test_01_add_address_and_card_pay(self):
        '''信用卡-新增地址-新增卡支付'''
        test_country = "Aruba"
        BaseSteps.del_all_address_and_cards(test_country)
        BaseSteps.one_step_to_pay(
            test_country, self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], 'Credit')
        payment.payment_page().click_confirm_to_pay()

        add_a_card.add_card_page().wait_page()
        add_a_card.add_card_page().input_card_number(self.test_data['card_number'])

        add_a_card.add_card_page().click_chose_date()
        add_a_card.add_card_page().swipe_to_chose_month(self.test_data['card_date_month'])
        add_a_card.add_card_page().swipe_to_chose_year(self.test_data['card_date_year'])
        add_a_card.add_card_page().click_date_confirm()
        add_a_card.add_card_page().input_card_cvv(self.test_data['card_cvv'])

        add_a_card.add_card_page().click_use_card()

        payment.payment_page().wait_confirm_page()

        self.assertTrue(self.d(
            resourceId="com.vova.android:id/try_again_btn", textContains='SHOP NOW').exists(timeout=2))
        self.wait_element_then_screenshot(
            self.d(resourceId="com.vova.android:id/try_again_btn", textContains='SHOP NOW'))
        if self.test_env != "test":
            self.d(resourceId="com.vova.android:id/check_your_order_btn").click()
            order_details.order_details_page().wait_page()
            log.i(self.d(resourceId="com.vova.android:id/order_no_tv").get_text() + '记得退款')

    # @unittest.skip
    @testcase
    def test_02_change_new_address_pay(self):
        '''波兰dotpay-地址切换为新增地址支付'''
        BaseSteps.one_step_to_checkout_without_coupon(
            "Poland", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'])
        BaseSteps.ensure_needed_country_and_address('Poland')

        checkout_v2.checkout_page().click_default_address()
        shipping_address.shipping_address_page().wait_page()
        shipping_address.shipping_address_page().click_setting_add_address_button()

        BaseSteps.add_shipping_address_in_order('dotpay')

        self.assertTrue(self.d(
            resourceId="com.vova.android:id/addressDesTv", textContains='dotpay').exists(timeout=2))

        BaseSteps.checkout_to_change_payment_method('Dotpay')
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/failure_tip_text"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/channelLabelTv"))

        BasePage().press_back_to_home()
        BaseSteps.go_shipping_address_edit_page("Poland")
        add_address_v2.add_address_page().click_del_button_for_address_v2()

    # @unittest.skip
    @testcase
    def test_03_change_exists_address_pay(self):
        '''印度net-banking-切换为已存在的地址支付'''
        BaseSteps.one_step_to_checkout_without_coupon(
            "India", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'])
        BaseSteps.ensure_needed_country_and_address('India')

        a = self.d(resourceId="com.vova.android:id/countryDesTv").get_text()
        log.i('原地址为：%s' % a)
        checkout_v2.checkout_page().click_default_address()

        shipping_address.shipping_address_page().wait_page()
        shipping_address.shipping_address_page().select_needed_address_with_text_and_index('India')

        checkout_v2.checkout_page().wait_page()
        self.d(resourceId="com.vova.android:id/countryDesTv", text=a).wait_gone(timeout=10.0)
        b = self.d(resourceId="com.vova.android:id/countryDesTv").get_text()
        log.i('新地址为：%s' % b)
        self.assertNotEqual(a, b)

        BaseSteps.checkout_to_change_payment_method("India Net Banking")
        payment.payment_page().input_pay_code("India Net Banking", self.PAN)
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="root"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="bank"))

    # @unittest.skip
    @testcase
    def test_04_login_to_checkout_pay(self):
        '''印度UPI-登录后支付'''
        BaseSteps.user_logout()
        BaseSteps.search_goods_by_id(self.test_data['normal_goods_id'])
        BaseSteps.buy_goods_with_attr(self.test_data['normal_goods_attr'])
        bag.bag_page().click_checkout_button()
        login.login_page().wait_page()
        login.login_page().login(self.test_data['user_name_02'], self.test_data['password_02'])

        checkout_v2.checkout_page().wait_page()
        BaseSteps.ensure_needed_country_and_address('India')
        BaseSteps.checkout_to_change_payment_method('UPI')

        payment.payment_page().input_pay_code("UPI", self.PAN)
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="root"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="tab-title"))

    # @unittest.skip
    @testcase
    def test_05_modify_address_pay(self):
        '''荷兰ideal-修改原地址支付'''
        if self.test_env == "test":
            attrs = None
        else:
            attrs = self.test_data['netherlands_goods_attr']
        BaseSteps.one_step_to_checkout_without_coupon(
            "Netherlands", self.test_data['netherlands_goods_id'], attrs=attrs)
        BaseSteps.ensure_needed_country_and_address('Netherlands')

        checkout_v2.checkout_page().click_default_address()
        shipping_address.shipping_address_page().wait_page()
        shipping_address.shipping_address_page().click_edit_button_for_address_v2()
        add_address_v2.add_address_page().input_address('updated')
        add_address_v2.add_address_page().click_save_button()

        checkout_v2.checkout_page().wait_page()

        self.assertTrue(self.d(
            resourceId="com.vova.android:id/addressDesTv", textContains='updated').exists(timeout=2))

        BaseSteps.checkout_to_change_payment_method("iDeal")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="android:id/message"))
        else:
            payment.payment_page().wait_payment_methods()
            payment.payment_page().click_ideal_pay()
            self.wait_element_then_screenshot(self.d(resourceId="nl.rabomobiel:id/message"))

        BasePage().press_back_to_home()
        BaseSteps.go_shipping_address_edit_page("Netherlands")
        add_address_v2.add_address_page().input_address(self.test_data['detail_address'])
        add_address_v2.add_address_page().click_save_button()

        self.assertTrue(self.d(resourceId="com.vova.android:id/addressDesTv",
                               textContains=self.test_data['detail_address']).exists(timeout=15))