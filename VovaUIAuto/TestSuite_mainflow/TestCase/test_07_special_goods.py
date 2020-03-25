#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Public.ReadConfig import ReadConfig
from PageObject import home, commodity_details, search, bag, checkout_v2, payment
from Public import BaseSteps
from Public.Decorator import *
from Public.Test_data import get_test_data


# @unittest.skip
class TestSpecialGoods(unittest.TestCase, BasePage):
    '''特殊商品测试'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.watch_device("Pretty Sure|Sure|Baik, saya paham.|GET IT!|总是允许|始终允许")
        cls.test_data = get_test_data(cls.d)
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
    def test_01_express_goods_flow(self):
        '''海外仓商品下单流程验证'''
        if self.test_env == "test":
            self.d.app_clear('com.vova.android')
            self.d.app_start("com.vova.android")
            BaseSteps.init_app_operation()
            BaseSteps.user_login(self.test_data['user_name_02'], self.test_data['password_02'])
        else:
            BaseSteps.change_country("France", self.test_data['normal_goods_id'], self.test_data['normal_goods_attr'])
            home.home_page().click_search_button()
            search.search_page().wait_page()
            search.search_page().click_search_box()
            search.search_page().wait_search_inner_page()
            search.search_page().click_inner_search_box()
            search.search_page().input_goods_id_to_search(self.test_data['express_good_id'])
            search.search_page().wait_goods_img()
            self.assertTrue(self.d(resourceId="com.vova.android:id/iv_over_sea_img").exists(timeout=4))
            search.search_page().click_item_img()
            commodity_details.commodity_details_page().click_more_attr_button()
            commodity_details.commodity_details_page().wait_attr_pop_up()
            self.assertTrue(self.d(resourceId="com.vova.android:id/iv_select_fbv").exists(timeout=4))
            commodity_details.commodity_details_page().chose_express_shipping()
            attrs = self.test_data['express_good_attr']
            for attr in attrs:
                commodity_details.commodity_details_page().select_goods_attr(attr)
            commodity_details.commodity_details_page().click_add_to_bag_button()
            bag.bag_page().wait_page()
            self.assertTrue(self.d(resourceId="com.vova.android:id/cl_express_ship").exists(timeout=4))
            bag.bag_page().click_checkout_button()
            checkout_v2.checkout_page().wait_page()
            self.assertTrue(self.d(resourceId="com.vova.android:id/goods_fast_img").exists(timeout=4))
            BasePage().press_back_to_home()
            BaseSteps.empty_shopping_bag()





