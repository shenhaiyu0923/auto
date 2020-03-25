#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from PageObject import home, shipping_address, add_address_v2
from Public import BaseSteps
from Public.Decorator import *
from Public.Test_data import get_test_data


# @unittest.skip
class TestUserActions(unittest.TestCase, BasePage):
    '''相关用户操作测试'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.test_data = get_test_data(cls.d)
        cls.watch_device("Pretty Sure|GET IT!|总是允许|始终允许|Homepage")

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
    def test_01_register(self):
        '''用户注册'''
        BaseSteps.user_register()

    # @unittest.skip
    @testcase
    def test_02_add_new_address_first(self):
        '''add_address新版页面首次新增地址并编辑'''
        BaseSteps.add_address_in_setting()
        # 编辑地址
        BasePage.wait_element_exists(self.d(resourceId='com.vova.android:id/addressModifyIv'))
        time.sleep(2)  # 兼容刷新不完成时点击编辑无效，待完善

        shipping_address.shipping_address_page().click_edit_button_for_address_v2()
        add_address_v2.add_address_page().wait_edit_page()
        add_address_v2.add_address_page().input_address('updated'+self.test_data['detail_address'])
        add_address_v2.add_address_page().click_save_button()
        a = self.d(resourceId="com.vova.android:id/addressDesTv", textContains='updated').exists(timeout=6)
        self.assertTrue(a)

    # @unittest.skip
    @testcase
    def test_03_add_new_address_no_first(self):
        '''add_address新版页面非首次新增地址并删除'''
        BaseSteps.add_address_in_setting()
        BasePage.wait_element_exists(self.d(resourceId='com.vova.android:id/addressModifyIv')[1])
        time.sleep(2)  # 兼容刷新不完成时点击编辑无效，待完善
        # 删除地址
        shipping_address.shipping_address_page().click_edit_button_for_address_v2()
        add_address_v2.add_address_page().wait_edit_page()
        add_address_v2.add_address_page().click_del_button_for_address_v2()

        BasePage.wait_element_exists(self.d(resourceId='com.vova.android:id/addressModifyIv'))
        self.d(resourceId="com.vova.android:id/addressDesTv", textContains='updated').wait_gone(timeout=4.0)
        self.assertFalse(self.d(
            resourceId="com.vova.android:id/addressDesTv", textContains='updated').exists())

    # @unittest.skip
    @testcase
    def test_04_logout(self):
        '''用户登出'''
        BaseSteps.user_logout()
        if BasePage.element_is_exists(self.d(resourceId="com.vova.android:id/tv_sign_in"), timeout=0) is False:
            self.find_element_by_swipe_down(self.d(resourceId="com.vova.android:id/tv_sign_in"))
        self.assertTrue(self.d(
            resourceId="com.vova.android:id/tv_sign_in", text='SIGN IN').exists(timeout=4))

    # @unittest.skip
    @testcase
    def test_05_login(self):
        '''用户登录'''
        home.home_page().wait_page()
        BaseSteps.user_login(self.test_data['user_name_01'], self.test_data['password_01'])
        self.wait_element_then_screenshot(self.d(resourceId="com.vova.android:id/tv_user_name"))
