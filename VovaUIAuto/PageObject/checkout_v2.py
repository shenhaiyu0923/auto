#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError
from PageObject import home, login, user_center, search, commodity_details, account_setting, bag, payment, checkout, \
    order_details, shipping_address, my_orders
from Public.BasePage import BasePage
from Public.Decorator import *
from Public.Test_data import get_test_data


class checkout_page(BasePage):

    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/address_title_tv").wait(timeout=15):
                pass
            else:
                raise Exception('Not in CheckoutPage')
        except Exception:
            raise Exception('Not in CheckoutPage')

    @teststep
    def click_place_order_button(self):
        self.d(resourceId="com.vova.android:id/place_order_btn", text="PLACE ORDER").click()
        log.i("点击Place Order按钮")
        self.d(resourceId="com.vova.android:id/place_order_btn", text="PLACE ORDER").wait_gone(timeout=15.0)
        if self.d(resourceId="com.vova.android:id/place_order_btn", text="PLACE ORDER").click_exists(timeout=1.0):
            log.i("二次点击Place Order按钮")  # 兼容低概率点不上的bug

    @teststep
    def click_deliver_to_country(self):
        self.d(resourceId="com.vova.android:id/country_name").click()
        log.i("点击目的国")

    @teststep
    def click_add_shipping_address_in_order(self):
        self.d(resourceId="com.vova.android:id/add_address_layout").click()
        log.i("点击新增邮寄地址")

    @teststep
    def click_coupons(self):
        self.d(resourceId="com.vova.android:id/coupons_root").click()
        log.i("点击优惠券")

    @teststep
    def click_address(self):
        self.d(resourceId="com.vova.android:id/sel_address_layout").click()
        log.i("点击地址栏")

    @teststep
    def is_exists_default_address(self, country_name):
        log.i('判断是否存在该国家下的地址')
        return self.element_is_exists(
            self.d(resourceId='com.vova.android:id/countryDesTv', textContains=country_name),
            timeout=5
        )

    @teststep
    def click_default_address(self):
        self.d(resourceId="com.vova.android:id/sel_address_layout").click()
        log.i("点击默认地址栏")

    @teststep
    def input_PAN(self, text):
        log.i("输入PAN：%s" % text)
        self.d(resourceId="com.vova.android:id/et_enter_pan").set_text(text)

    @teststep
    def get_current_country(self):
        return self.d(resourceId='com.vova.android:id/country_name').get_text()

    @teststep
    def click_change_country(self):
        self.d(text='DELIVER TO').click()