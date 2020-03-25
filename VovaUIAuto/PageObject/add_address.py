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
            if self.d(resourceId="com.vova.android:id/title_text", text="Add address").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Add Address Page')
        except Exception:
            raise Exception('Not in Add Address Page')

    @teststep
    def wait_edit_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text="Edit address").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Edit Address Page')
        except Exception:
            raise Exception('Not in Edit Address Page')

    @teststep
    def click_save_button(self):
        # self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/addLayout"))
        self.d(resourceId="com.vova.android:id/lv_add_new_address").click()
        log.i("点击Save按钮")

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
    def click_add_button(self):
        self.d(resourceId="com.vova.android:id/tv_submit").click()
        log.i("点击Add按钮")

    @teststep
    def click_confirm_button(self):
        self.d(resourceId="com.vova.android:id/tv_address_save").click_exists(timeout=2.0)
        log.i("点击Confirm按钮")

    @teststep
    def input_last_name(self, text):
        self.d(resourceId="com.vova.android:id/tiet_last_name").set_text(text)
        log.i("输入名字")

    @teststep
    def input_first_name(self, text):
        self.d(resourceId="com.vova.android:id/tiet_first_name").set_text(text)
        log.i("输入姓")

    @teststep
    def input_phone(self, text):
        self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/tiet_phone_number"))
        self.d(resourceId="com.vova.android:id/tiet_phone_number").set_text(text)
        log.i("输入电话号码")

    @teststep
    def input_state(self, text):
        self.d(resourceId="com.vova.android:id/tiet_state").set_text(text)
        log.i("输入所在州")

    @teststep
    def input_city(self, text):
        self.d(resourceId="com.vova.android:id/tiet_city").set_text(text)
        log.i("输入所在城市")

    @teststep
    def input_address(self, text):
        self.d(resourceId="com.vova.android:id/tiet_address").set_text(text)
        log.i("输入详细住址")

    @teststep
    def input_address_optional(self, text):
        self.d(resourceId="com.vova.android:id/tiet_address2").set_text(text)
        log.i("输入详细住址第二行")

    @teststep
    def input_zip_code(self, text):
        self.d(resourceId="com.vova.android:id/tiet_zip_post_code").set_text(text)
        log.i("输入邮编")

    @teststep
    def press_back(self):
        self.watch_device("Pretty Sure")
        self.d.press("back")
        time.sleep(0.5)
        self.unwatch_device()


