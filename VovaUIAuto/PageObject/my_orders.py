#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class my_orders_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text="My Orders").wait(timeout=15):
                pass
            else:
                raise Exception('Not in MyOrdersPage')
        except Exception:
            raise Exception('Not in MyOrdersPage')

    @teststep
    def click_pay_button(self, index=0):
        self.d(resourceId="com.vova.android:id/layout_unpaid_btn", instance=index).click()
        log.i("点击Pay按钮")

    @teststep
    def click_unpaid_button(self, index=0):
        self.d(resourceId="com.vova.android:id/order_display_status_text", instance=index).click()
        log.i("点击查看订单详情")
