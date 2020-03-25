#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest

from PageObject import home, login, user_center, search, commodity_details, account_setting, bag, payment, checkout, \
    order_details, shipping_address, my_orders
from Public.BasePage import BasePage
from Public.Decorator import *
from Public.Test_data import get_test_data


@unittest.skip
class TestBuyAndPay(unittest.TestCase, BasePage):
    '''各种支付测试'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        # cls.d.app_start("com.vova.android")  # restart app
        cls.test_data = get_test_data(cls.d)
        cls.PAN = "EHFGA5967A"
        cls.watch_device("Sure|Baik, saya paham.")

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        # cls.d.app_stop("com.vova.android")  # restart app
        cls.unwatch_device()

    @setup
    def setUp(self):
        self.d.app_start("com.vova.android")  # restart app

    @teardown
    def tearDown(self):
        self.d.app_stop("com.vova.android")  # restart app

    # @unittest.skip
    @testcase
    def test_01_normal_goods_paid_by_card(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("United States")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("United States")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    # @unittest.skip
    @testcase
    def test_02_normal_goods_paid_by_boleto_Brazil(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Brazil")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("Brazil")
        checkout.checkout_page().change_payment_method("Boleto")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    # @unittest.skip
    @testcase
    def test_03_normal_goods_paid_by_dotpay_Poland(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Poland")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("poland")
        checkout.checkout_page().change_payment_method("Dotpay")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    # @unittest.skip
    @testcase
    def test_04_normal_goods_paid_by_ideal_Netherlands(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Netherlands")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['cod_goods_id'])
        buy_goods_with_attr(self.test_data['cod_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("netherlands")
        checkout.checkout_page().change_payment_method("iDeal")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    @testcase
    def test_05_normal_goods_india(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("India")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("india")
        checkout.checkout_page().change_payment_method("UPI")
        checkout.checkout_page().input_PAN(self.PAN)
        self.set_original_ime()
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

        self.press_back_until_special_element('com.vova.android:id/check_button')
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        checkout.checkout_page().change_payment_method("India Net Banking")
        checkout.checkout_page().input_PAN(self.PAN)
        self.set_original_ime()
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    @testcase
    def test_06_normal_goods_indonesia(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Indonesia")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("Indonesia")
        checkout.checkout_page().change_payment_method("Bank Transfers")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

        self.press_back_until_special_element('com.vova.android:id/check_button')
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        checkout.checkout_page().change_payment_method("Alfamart")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

        self.press_back_until_special_element('com.vova.android:id/check_button')
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        checkout.checkout_page().change_payment_method("OVO CASH")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    @testcase
    def test_07_normal_goods_Russia(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Russian Federation")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("Russia")
        checkout.checkout_page().change_payment_method("QIWI Wallet ")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

        self.press_back_until_special_element('com.vova.android:id/check_button')
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        checkout.checkout_page().change_payment_method("Yandex Money")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    @testcase
    def test_08_normal_goods_Germany(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Germany")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("Germany")
        checkout.checkout_page().change_payment_method("SOFORT")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    @unittest.skip
    @testcase
    def test_09_normal_goods_Morocco(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Morocco")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['normal_goods_id'])
        buy_goods_with_attr(self.test_data['normal_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("Morocco")
        checkout.checkout_page().change_payment_method("Anmnpay")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()

    # @unittest.skip
    @testcase
    def test_10_normal_goods_COD(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        change_country("Kuwait")
        self.press_back_to_home()

        home.home_page().click_search_button()
        search_goods_by_id(self.test_data['cod_goods_id'])
        buy_goods_with_attr_by_cod(self.test_data['cod_goods_attr'])

        bag.bag_page().wait_page()
        bag.bag_page().click_checkout_button()

        checkout.checkout_page().wait_page()
        change_shipping_address_with_country("Kuwait")
        checkout.checkout_page().change_payment_method("Cash On Delivery")
        checkout.checkout_page().click_place_order_button()
        time.sleep(10.0)
        self.screenshot()


def search_goods_by_id(goods_id):
    search.search_page().wait_page()
    search.search_page().click_search_box()
    search.search_page().click_inner_search_box()
    search.search_page().input_goods_id_to_search(goods_id)
    search.search_page().click_item_img()


def buy_goods_with_attr(attrs):
    commodity_details.commodity_details_page().wait_page()
    commodity_details.commodity_details_page().click_bag_button()
    for attr in attrs:
        commodity_details.commodity_details_page().select_goods_attr(attr)
    commodity_details.commodity_details_page().click_add_amount_button()
    commodity_details.commodity_details_page().click_add_to_bag_button()


def buy_goods_with_attr_by_cod(attrs):
    commodity_details.commodity_details_page().wait_page()
    commodity_details.commodity_details_page().click_bag_button()
    for attr in attrs:
        commodity_details.commodity_details_page().select_goods_attr(attr)
    commodity_details.commodity_details_page().click_add_to_bag_button()
    bag.bag_page().wait_page()
    while not bag.bag_page().is_cod():
        commodity_details.commodity_details_page().click_add_amount_button()
        time.sleep(0.5)


def change_country(country_name):
    user_center.user_page().wait_page()
    user_center.user_page().click_setting_button()

    account_setting.account_setting_page().wait_page()
    account_setting.account_setting_page().open_country_list()
    account_setting.account_setting_page().search_country(country_name)
    account_setting.account_setting_page().select_country(country_name)

    # while not TestBuyAndPay().d(resourceId="com.vova.android:id/bottom_container").exists():
    #     TestBuyAndPay().d.press('back')
    #     time.sleep(0.5)

    # home.home_page().click_home_button()


def change_shipping_address_with_country(country_name):
    checkout.checkout_page().click_default_address()
    shipping_address.shipping_address_page().wait_page()
    shipping_address.shipping_address_page().select_default_address(country_name)
    checkout.checkout_page().wait_page()