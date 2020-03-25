#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Public.ReadConfig import ReadConfig
from PageObject import payment, paypal, order_details
from Public.Decorator import *
from Public import BaseSteps
from Public.Test_data import get_test_data


# @unittest.skip
class TestBuyAndPay(unittest.TestCase, BasePage):
    '''常规支付测试'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.test_data = get_test_data(cls.d)
        cls.PAN = "qwert1423q"
        cls.CPF = '12649239700'
        cls.watch_device("Pretty Sure|Sure|Baik, saya paham.")
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
    def test_01_normal_goods_paid_by_card(self):
        '''信用卡支付'''
        BaseSteps.one_step_to_pay(
            "Angola", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], 'Credit')
        payment.payment_page().click_confirm_to_pay()
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
    def test_02_normal_goods_paid_by_paypal(self):
        '''PayPal支付-(测试环境沙盒支付)'''
        BaseSteps.one_step_to_pay(
            "Angola", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "PayPal")
        if self.test_env == "test":
            payment.payment_page().click_confirm_to_pay()
            paypal.paypal_sandbox_page().wait_page()
            paypal.paypal_sandbox_page().click_proceed_button()

            self.assertTrue(self.d(
                resourceId="com.vova.android:id/title_text", textContains='Confirmation').exists(timeout=15))
            self.wait_element_then_screenshot(self.d(
                resourceId="com.vova.android:id/title_text", textContains='Confirmation'))
        else:
            self.screenshot()  # 正式需要paypal账号

    # @unittest.skip
    @testcase
    def test_03_normal_goods_paid_by_paypal_swipe(self):
        '''PayPal滑动支付(支持美国、印尼、西班牙)'''
        if self.test_env == "test":
            BaseSteps.one_step_to_pay(
                "United States", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "PayPal")
            payment.payment_page().swipe_to_pay()

            self.assertTrue(self.d(
                resourceId="com.vova.android:id/title_text", textContains='Confirmation').exists(timeout=15))
            self.wait_element_then_screenshot(self.d(
                resourceId="com.vova.android:id/title_text", textContains='Confirmation'))

    @unittest.skip
    @testcase
    def test_04_normal_goods_paid_by_Amanpay_Morocco(self):
        '''摩洛哥GiroPay支付(线上暂没配置)'''
        BaseSteps.one_step_to_pay(
            "Morocco", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "Amanpay")
        payment.payment_page().click_confirm_to_pay()

        self.wait_element_then_screenshot(self.d(
            resourceId="com.vova.android:id/title_text", textContains='Confirmation'))

    # @unittest.skip
    @testcase
    def test_05_normal_goods_paid_by_dotpay_Poland(self):
        '''波兰dotpay支付'''
        BaseSteps.one_step_to_pay(
            "Poland", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], 'dotpay')
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/failure_tip_text"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/channelLabelTv"))

    # @unittest.skip
    @testcase
    def test_06_normal_goods_paid_by_EPS_Austria(self):
        '''奥地利GiroPay支付(测试环境暂无)'''
        if self.test_env != "test":
            BaseSteps.one_step_to_pay(
                "Austria", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "EPS")
            payment.payment_page().click_confirm_to_pay()
            self.wait_element_then_screenshot(self.d(resourceId="counter"))

    # @unittest.skip
    @testcase
    def test_07_normal_goods_paid_by_UPI_india(self):
        '''印度UPI支付'''
        BaseSteps.one_step_to_pay(
            "India", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "UPI")
        payment.payment_page().input_pay_code("UPI", self.PAN)
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="root"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="tab-title"))

    # @unittest.skip
    @testcase
    def test_08_normal_goods_paid_by_Banking_india(self):
        '''印度net_banking支付'''
        BaseSteps.one_step_to_pay(
            "India", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "India Net Banking")
        payment.payment_page().input_pay_code("India Net Banking", self.PAN)
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="root"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="bank"))

    # @unittest.skip
    @testcase
    def test_09_normal_goods_paid_by_Bank_Transfers_indonesia(self):
        '''印尼bank_transfers支付'''
        BaseSteps.one_step_to_pay(
            "Indonesia", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "Bank Transfers")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(text="GO BACK"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="invoice-pending-left-content"))

    # @unittest.skip
    @testcase
    def test_10_normal_goods_paid_by_OVO_indonesia(self):
        '''印尼OVO_CASH支付'''
        BaseSteps.one_step_to_pay(
            "Indonesia", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "OVO")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(text="GO BACK"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="invoice-pending-left-content"))

    # @unittest.skip
    @testcase
    def test_11_normal_goods_paid_by_Yandex_indonesia(self):
        '''俄罗斯Yandex_Money支付'''
        BaseSteps.one_step_to_pay("Russian Federation", self.test_data['normal_goods_id'],
                             self.test_data['normal_goods_attr'], "Yandex Money")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="android:id/message"))
        else:
            payment.payment_page().wait_payment_methods()
            payment.payment_page().click_payment_methods()
            self.wait_element_then_screenshot(self.d(resourceId="android:id/content"))

    # @unittest.skip
    @testcase
    def test_12_normal_goods_paid_by_QIWI_indonesia(self):
        '''俄罗斯QIWI_Wallet支付'''
        BaseSteps.one_step_to_pay(
            "Russian Federation", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "QIWI Wallet")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="android:id/message"))
        else:
            payment.payment_page().wait_payment_methods()
            payment.payment_page().click_payment_methods()
            self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/button_continue"))

    # @unittest.skip
    @testcase
    def test_13_normal_goods_paid_by_Sofort_Germany(self):
        '''德国Sofort支付'''
        BaseSteps.one_step_to_pay(
            "Germany", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "SOFORT")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="android:id/message"))
        else:
            payment.payment_page().wait_payment_methods()
            payment.payment_page().click_payment_methods()
            self.wait_element_then_screenshot(self.d(resourceId="android:id/content"))

    # @unittest.skip
    @testcase
    def test_14_normal_goods_paid_by_GiroPay_Germany(self):
        '''德国GiroPay支付'''
        BaseSteps.one_step_to_pay(
            "Germany", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "GiroPay")
        payment.payment_page().click_confirm_to_pay()

        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="android:id/message"))
        else:
            payment.payment_page().wait_payment_methods()
            payment.payment_page().click_payment_methods()
            self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/button_continue"))

    # @unittest.skip
    @testcase
    def test_15_normal_goods_paid_by_PayLater_Germany(self):
        '''德国PayLater支付'''
        BaseSteps.one_step_to_pay(
            "Germany", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "Later")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="klarna-payments__payment-options"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="invoice"))

    # @unittest.skip
    @testcase
    def test_16_normal_goods_paid_by_SliceIt_Germany(self):
        '''德国SliceIt支付'''
        BaseSteps.one_step_to_pay(
            "Germany", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "Slice")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="klarna-payments__payment-options"))
        else:
            self.wait_element_then_screenshot(self.d(resourceId="base-account-bullets__container"))

    # @unittest.skip
    @testcase
    def test_17_normal_goods_paid_by_boleto_Brazil(self):
        '''巴西Boleto支付'''
        BaseSteps.one_step_to_pay(
            "Brazil", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'], "Boleto")
        payment.payment_page().input_pay_code("Boleto", self.CPF)
        payment.payment_page().click_confirm_to_pay()
        self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/ll_copy_bar_code"))

    @unittest.skip
    @testcase
    def test_18_cod_goods_paid_by_COD(self):
        '''科威特COD支付(已去除该种支付方式)'''
        BaseSteps.one_step_to_pay(
            "Kuwait", self.test_data['cod_goods_id'], self.test_data['cod_goods_attr'], "Cash On Delivery")
        self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/ll_copy_bar_code"))

    # @unittest.skip
    @testcase
    def test_19_netherlands_goods_paid_by_ideal_Netherlands(self):
        '''荷兰ideal支付'''
        if self.test_env == "test":
            BaseSteps.one_step_to_pay(
                "Netherlands", self.test_data['netherlands_goods_id'], None, "iDeal")
        else:
            BaseSteps.one_step_to_pay(
                "Netherlands", self.test_data['netherlands_goods_id'], self.test_data['netherlands_goods_attr'], "iDeal")
        payment.payment_page().click_confirm_to_pay()
        if self.test_env == "test":
            self.wait_element_then_screenshot(self.d(resourceId="android:id/message"))
        else:
            payment.payment_page().wait_payment_methods()
            payment.payment_page().click_ideal_pay()
            self.wait_element_then_screenshot(self.d(resourceId="nl.rabomobiel:id/message"))
