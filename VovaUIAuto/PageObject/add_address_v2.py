#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class add_address_page(BasePage):
    @teststep
    def wait_add_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text="Add Address").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Add Address Page')
        except Exception:
            raise Exception('Not in Add Address Page')

    @teststep
    def wait_edit_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text="Edit Address").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Edit Address Page')
        except Exception:
            raise Exception('Not in Edit Address Page')

    @teststep
    def click_save_button(self):
        # self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/addLayout"))
        self.d(resourceId="com.vova.android:id/addLayout").click()
        log.i("点击Save按钮")

    @teststep
    def input_last_name(self, text):
        self.find_element_by_child("LAST NAME", "android.widget.LinearLayout", "android.widget.EditText").set_text(text)
        log.i("输入名字")

    @teststep
    def input_first_name(self, text):
        self.find_element_by_child("FIRST NAME", "android.widget.LinearLayout",
                                   "android.widget.EditText").set_text(text)
        log.i("输入姓")

    @teststep
    def input_phone(self, text):
        self.find_element_by_child("PHONE NUMBER", "android.widget.LinearLayout",
                                   "android.widget.EditText").set_text(text)
        log.i("输入电话号码")

    @teststep
    def is_email_exists(self):
        log.i("判断必填项是否存在邮箱")
        return self.element_is_exists(self.d(text="EMAIL"), timeout=1)

    @teststep
    def input_email(self, text):
        self.find_element_by_child("EMAIL", "android.widget.LinearLayout",
                                   "android.widget.EditText").set_text(text)
        log.i("输入邮箱")

    @teststep
    def input_state(self, text):
        a = self.find_element_by_child("STATE", "android.widget.LinearLayout", "android.widget.EditText")
        if self.element_is_exists(a):
            a.set_text(text)
        else:
            self.d(text="STATE").sibling(className='android.widget.ImageView').click()
            self.d(resourceId="com.vova.android:id/titleTv", text="Please Select").wait(timeout=15)
            self.d(resourceId="com.vova.android:id/tv_name")[0].click(timeout=15)
            time.sleep(1)  # 兼容选择洲后，页面是刷新状态，无法set_text
        log.i("输入所在州")

    @teststep
    def input_city(self, text):
        a = self.find_element_by_child("CITY", "android.widget.LinearLayout", "android.widget.EditText")
        if self.element_is_exists(a):
            a.set_text(text)
        else:
            self.d(text="CITY").sibling(className='android.widget.ImageView').click()
            self.d(resourceId="com.vova.android:id/titleTv", text="Please Select").wait(timeout=15)
            self.d(resourceId="com.vova.android:id/tv_name")[0].click(timeout=15)
            time.sleep(1)
        log.i("输入所在城市")

    @teststep
    def input_address(self, text):
        self.find_element_by_child("ADDRESS", "android.widget.LinearLayout",
                                   "android.widget.EditText").set_text(text)
        log.i("输入ADDRESS")

    @teststep
    def input_zip_code(self, text):
        self.find_element_by_child("ZIP CODE", "android.widget.LinearLayout",
                                   "android.widget.EditText").set_text(text)
        log.i("输入邮编")

    @teststep
    def click_default_address_button(self):
        self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/shipping_default"))
        self.d(resourceId="com.vova.android:id/shipping_default").click()
        log.i("点击是否设置为默认地址按钮")

    @teststep
    def click_default_billing_button(self):
        self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/billing_default"))
        self.d(resourceId="com.vova.android:id/billing_default").click()
        log.i("点击是否设置为默认账单按钮")

    @teststep
    def click_save_button(self):
        self.find_element_by_swipe_up(self.d(text="SAVE"))
        self.d(text="SAVE").click_exists(timeout=2.0)
        log.i("点击SAVE按钮")

    @teststep
    def press_back(self):
        self.watch_device("Pretty Sure")
        self.d.press("back")
        time.sleep(0.5)
        self.unwatch_device()

    @teststep
    def click_del_button_for_address_v2(self):
        self.d(resourceId="com.vova.android:id/iv_delete").click()
        log.i("点击删除地址按钮")