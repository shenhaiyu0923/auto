#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class order_details_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/order_support_type", text='OTHER DETAILS').wait(timeout=15):
                pass  # 兼容刷新状态下点击编辑无效，刷新完成时没这个元素才会出现，恰好兼容刷新完成状态，后点击
            else:
                raise Exception('Not in OrderDetailsPage')
        except Exception:
            raise Exception('Not in OrderDetailsPage')

    @teststep
    def click_pay_button(self):
        self.d(resourceId="com.vova.android:id/check_button", text="PAY").click_exists()
        log.i("点击PAY按钮")

    @teststep
    def click_pay_button_v2(self):
        self.d(resourceId="com.vova.android:id/check_button").click()
        log.i("点击PAY按钮")

    @teststep
    def get_order_id(self):
        if not self.d(resourceId='com.vova.android:id/order_no_tv').exists(timeout=2):
            self.swipe_up()
        return self.d(resourceId='com.vova.android:id/order_no_tv').get_text()

    @teststep
    def click_edit_address_button(self):
        self.d(resourceId="com.vova.android:id/address_edit_img").click()
        log.i("点击编辑地址按钮")

