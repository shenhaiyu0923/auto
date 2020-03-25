#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class checkout_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text="Checkout").wait(timeout=15):
                pass
            else:
                raise Exception('Not in CheckoutPage')
        except Exception:
            raise Exception('Not in CheckoutPage')

    @teststep
    def click_place_order_button(self):
        time.sleep(1.0)
        self.d(resourceId="com.vova.android:id/progressBar").wait_gone(timeout=15.0)
        self.d(resourceId="com.vova.android:id/buy_text_view").click()
        log.i("点击Place Order按钮")

    @teststep
    def click_deliver_to_country(self):
        self.d(resourceId="com.vova.android:id/country_name").click()
        log.i("点击目的国")

    @teststep
    def add_shipping_address_in_order(self):
        self.d(resourceId="com.vova.android:id/add_address_layout").click_exists()
        log.i("新增邮寄地址")

    @teststep
    def click_coupons(self):
        self.d(resourceId="com.vova.android:id/coupons_root").click()
        log.i("点击优惠券")

    @teststep
    def click_address(self):
        self.d(resourceId="com.vova.android:id/sel_address_layout").click()
        log.i("点击地址栏")

    @teststep
    def click_default_address(self):
        self.d(resourceId="com.vova.android:id/sel_address_layout").click()
        log.i("点击默认地址栏")

    @teststep
    def change_payment_method(self, method):
        if self.d(resourceId="com.vova.android:id/pay_text", text=method).sibling(
                className="android.widget.ImageView", resourceId="com.vova.android:id/payment_sel").\
                click_exists(timeout=1.0):
            log.i("成功选择付款方式：" + method)
        else:
            log.i("未找到指定的付款方式：" + method)

    @teststep
    def input_PAN(self, text):
        log.i("输入PAN：" + text)
        self.d(resourceId="com.vova.android:id/et_enter_pan").set_text(text)

