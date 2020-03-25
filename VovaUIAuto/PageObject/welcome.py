#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class welcome_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/tv_welcome").wait(timeout=15):
                return True
            else:
                raise Exception('Not in WelcomePage')
        except Exception:
            raise Exception('Not in WelcomePage')

    @teststep
    # gender: male, female
    def select_gender(self, gender):
        log.i('选择性别')
        self.d(resourceId="com.vova.android:id/rl_"+gender+"_layout").click()

    @teststep
    # age:under_18, 18_to_30, 31_to_45, up_45
    def choose_age(self, age):
        log.i('选择年龄区间')
        self.d(resourceId="com.vova.android:id/rl_" + age + "_layout").click()

    @teststep
    def click_skip(self):
        log.i('跳过选择年龄区间')
        self.d(resourceId="com.vova.android:id/ll_skip_layout").click()
