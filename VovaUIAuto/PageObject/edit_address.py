#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class edit_address_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(text="ADDRESS DETAILS").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Edit Address Page')
        except Exception:
            raise Exception('Not in Edit Address Page')

    @teststep
    def input_address(self, text):
        self.find_element_by_child("ADDRESS", "android.widget.LinearLayout",
                                   "android.widget.EditText").clear_text()
        self.find_element_by_child("ADDRESS", "android.widget.LinearLayout",
                                   "android.widget.EditText").set_text(text)
        log.i("输入ADDRESS:%s" % text)

    @teststep
    def click_save_button(self):
        self.find_element_by_swipe_up(self.d(text="SAVE"))
        self.d(text="SAVE").click_exists(timeout=2.0)
        log.i("点击SAVE按钮")
