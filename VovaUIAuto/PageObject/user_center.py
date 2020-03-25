#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class user_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/tv_recently_view").wait(timeout=15):
                return True
            else:
                raise Exception('Not in user page')
        except Exception:
            raise Exception('Not in user page')

    @teststep
    def wait_is_login_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/tv_user_name").wait(timeout=15):
                return True
            else:
                raise Exception('Not in is_login user page')
        except Exception:
            raise Exception('Not in is_login user page')

    @teststep
    def discover_user_name(self):
        while self.d(resourceId="com.vova.android:id/tv_user_name").exists(timeout=3) is False:
            self.swipe_down()
            self.d(resourceId="com.vova.android:id/tv_user_name").exists(timeout=3)
        log.i('刷新登录成功状态')

    @teststep
    def wait_get_it_gone(self):
        self.d(resourceId="com.vova.android:id/tv_get_it").wait_gone(timeout=10.0)

    @teststep
    def is_page(self):
        if self.d(resourceId="com.vova.android:id/tv_my_orders").wait(timeout=1):
            return True
        else:
            return False

    @teststep
    def click_GetIt_button(self):
        log.i("点击Get it按钮")
        self.d(resourceId="com.vova.android:id/tv_get_it").click()

    @teststep
    def click_signin_button(self):
        if BasePage.element_is_exists(self.d(resourceId="com.vova.android:id/tv_sign_in"), timeout=0) is False:
            self.find_element_by_swipe_down(self.d(resourceId="com.vova.android:id/tv_sign_in"))
        self.d(resourceId="com.vova.android:id/tv_sign_in").click()
        log.i("点击SIGN IN按钮")
        self.d(resourceId="com.vova.android:id/tv_sign_in").wait_gone(timeout=1.0)
        if self.d(resourceId="com.vova.android:id/tv_sign_in").click_exists(timeout=1.0):
            log.i("二次点击SIGN IN按钮")  # 兼容低概率点不上的bug

    @teststep
    def clear_GetIt(self):
        while self.d(resourceId="com.vova.android:id/tv_get_it").wait(timeout=3):
            self.click_GetIt_button()

    @teststep
    def click_setting_button(self):
        if BasePage.element_is_exists(self.d(text="YOU MIGHT LIKE"), timeout=0) is False:
            self.find_element_by_swipe_up(self.d(text="YOU MIGHT LIKE"))  # 往下拉一拉再点，兼容点不上的情况
            log.i("经上滑已发现setting位置")
        self.d(resourceId="com.vova.android:id/tv_setting", text='Settings').click()
        log.i("点击Setting按钮")
        self.d(resourceId="com.vova.android:id/tv_setting", text='Settings').wait_gone(timeout=1.0)
        if self.d(resourceId="com.vova.android:id/tv_setting", text='Settings').click_exists(timeout=1.0):
            log.i("二次点击Setting按钮")  # 兼容低概率点不上的bug

    @teststep
    def click_my_orders_button(self):
        if BasePage.element_is_exists(
                self.d(resourceId="com.vova.android:id/tv_my_orders_view_all"), timeout=1) is False:
            self.find_element_by_swipe_down(self.d(resourceId="com.vova.android:id/tv_my_orders_view_all"))
            time.sleep(.5)
        self.d(resourceId="com.vova.android:id/tv_my_orders_view_all").click()
        log.i("点击orders列表按钮")
        self.d(resourceId="com.vova.android:id/tv_my_orders_view_all").wait_gone(timeout=1.0)
        if self.d(resourceId="com.vova.android:id/tv_my_orders_view_all").click_exists(timeout=1.0):
            log.i("二次点击orders列表按钮")  # 兼容低概率点不上的bug

