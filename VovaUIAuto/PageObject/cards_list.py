#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class cards_list_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text="My credit/debit cards").wait(timeout=15):
                pass
            else:
                raise Exception('Not in ShippingAddressPage')
        except Exception:
            raise Exception('Not in ShippingAddressPage')

    @teststep
    def click_card(self):
        log.i('点击卡片')
        self.d(resourceId="com.vova.android:id/card_number_tv").click()

    @teststep
    def wait_delete_button(self):
        try:
            if self.d(resourceId="com.vova.android:id/credit_delete_btn").wait(timeout=3):
                pass
            else:
                raise Exception('Not show delete btn')
        except Exception:
            raise Exception('Not show delete btn')

    @teststep
    def click_delete_button(self):
        log.i('点击删除')
        self.d(resourceId="com.vova.android:id/credit_delete_btn").click()

    @teststep
    def is_card_exists(self):
        return BasePage.element_is_exists(
            self.d(resourceId="com.vova.android:id/hint_tv", textContains='Opps'), timeout=.5)

    @teststep
    def wait_card_miss(self):
        log.i('等待卡片消失')
        self.d(resourceId="com.vova.android:id/card_number_tv").wait_gone(timeout=2.0)
