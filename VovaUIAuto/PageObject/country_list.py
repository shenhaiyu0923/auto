#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class country_list_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/country_divide_text").wait(timeout=15):
                pass
            else:
                raise Exception('Not in account setting page')
        except Exception:
            raise Exception('Not in account setting page')

    @teststep
    def search_country(self, country_name):
        self.d(resourceId="com.vova.android:id/edit_text").set_text(country_name)
        # self.d.send_action("search")
        log.i("搜索目标国家:" + country_name)

    @teststep
    def select_country(self, country_name):
        self.d(resourceId="com.vova.android:id/country_name", text=country_name).click(timeout=1.0)

    @teststep
    def ensure_country(self):
        self.d(resourceId="com.vova.android:id/rightText", text='DONE').click(timeout=1.0)
        log.i("选中目标国家")