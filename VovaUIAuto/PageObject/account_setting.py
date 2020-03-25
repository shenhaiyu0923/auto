#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class account_setting_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", textContains="Account").wait(timeout=15):
                pass
            else:
                raise Exception('Not in SettingPage')
        except Exception:
            raise Exception('Not in SettingPage')

    @teststep
    def click_sign_out_button(self):
        self.d(resourceId="com.vova.android:id/settings_tv_sign_in").click_exists(timeout=1.0)
        log.i("点击Sign Out按钮")

    @teststep
    def open_country_list(self):
        self.d(text="Country/Region").click()
        log.i("点击Country/Region按钮")

    @teststep
    def open_language_list(self):
        self.d(text="Language").click()
        log.i("点击Language按钮")

    @teststep
    def open_address_list(self):
        self.d(text="Shipping Address").click()
        log.i("点击Shipping Address按钮")

    @teststep
    def open_cards_list(self):
        self.d(text="My credit/debit cards").click()
        log.i("点击My credit/debit cards按钮")

