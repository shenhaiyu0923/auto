#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest

from PageObject import home, login, user_center, search, commodity_details
from Public.BasePage import BasePage
from Public.Decorator import *
from Public.Test_data import get_test_data


def creat_random_email():
    return ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
         'e', 'd', 'c', 'b', 'a'], 10)) + '@tetx.com'


class TestLogin(unittest.TestCase, BasePage):
    '''用户登录测试'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_start("com.vova.android")
        cls.test_data = get_test_data(cls.d)

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.vova.android")

    @setup
    def setUp(self):
        pass

    @teardown
    def tearDown(self):
        pass

    @unittest.skip
    @testcase
    def test_01_login(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        user_center.user_page().wait_page()
        user_center.user_page().clear_GetIt()
        user_center.user_page().click_signin_button()
        login.login_page().wait_page()
        self.set_fastinput_ime()
        login.login_page().input_username(self.test_data['user_name'])
        login.login_page().input_password(self.test_data['password'])
        login.login_page().click_login_btn()
        self.back()

    @unittest.skip
    @testcase
    def test_02_register(self):
        home.home_page().wait_page()
        home.home_page().click_account_button()
        user_center.user_page().wait_page()
        user_center.user_page().clear_GetIt()
        user_center.user_page().click_signin_button()
        login.login_page().wait_page()
        login.login_page().click_register_btn()
        self.set_fastinput_ime()
        login.login_page().input_first_name(self.test_data['first_name'])
        login.login_page().input_last_name(self.test_data['last_name'])
        login.login_page().input_email(creat_random_email())
        login.login_page().input_register_password(self.test_data['register_password'])
        login.login_page().input_confirm_register_password(self.test_data['register_password'])
        login.login_page().click_login_btn()
        self.watch_device("Shop Now")
        self.unwatch_device()
        time.sleep(10)

    @testcase
    def test_03_try(self):
        self.d(resourceId="com.vova.android:id/pay_title_tv", text="PayPal").sibling(className="android.widget.ImageView")[1].click()
        home.home_page().wait_page()
        home.home_page().click_search_button()
        search.search_page().wait_page()
        search.search_page().click_search_box()
        search.search_page().click_inner_search_box()
        search.search_page().input_goods_id_to_search("123456")
