#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class login_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(text="REGISTER").wait(timeout=15):
                return True
            else:
                raise Exception('Not in LoginPage')
        except Exception:
            raise Exception('Not in LoginPage')

    @teststep
    # 通用输入函数
    def input_by_id(self, text, item_id):
        log.i('输入:%s' % text)
        self.d(resourceId=item_id).set_text(text)

    @teststep
    def input_username(self, text):
        log.i('输入用户名:%s' % text)
        self.d(resourceId="com.vova.android:id/et_account").set_text(text)

    @teststep
    def input_password(self, text):
        log.i('输入密码:%s' % text)
        self.d(resourceId="com.vova.android:id/et_psw").set_text(text)

    @teststep
    def click_login_btn(self):
        log.i('点击注册提交按钮')
        self.d(resourceId="com.vova.android:id/btn_submit").click()

    @teststep
    def click_register_btn(self):
        log.i('点击注册按钮')
        self.d(resourceId="com.vova.android:id/tv_go_register").click()

    @teststep
    def input_first_name(self, text):
        log.i('输入姓:%s' % text)
        self.d(resourceId="com.vova.android:id/et_register_first_name").set_text(text)

    @teststep
    def input_last_name(self, text):
        log.i('输入名字:%s' % text)
        self.d(resourceId="com.vova.android:id/et_register_last_name").set_text(text)

    @teststep
    def input_email(self, text):
        log.i('输入邮箱:%s' % text)
        self.d(resourceId="com.vova.android:id/et_register_email").set_text(text)

    @teststep
    def input_register_password(self, text):
        log.i('输入密码:%s' % text)
        self.d(resourceId="com.vova.android:id/et_register_psw").set_text(text)

    @teststep
    def input_confirm_register_password(self, text):
        log.i('确认密码:%s' % text)
        self.d(resourceId="com.vova.android:id/et_register_psw_again").set_text(text)

    @teststep
    def choose_birthday(self):
        log.i("选择生日")
        self.d(resourceId="com.vova.android:id/btn_register_birthday").click()
        if self.d(resourceId="com.vova.android:id/btnApply").wait(timeout=3):
            self.d(resourceId="com.vova.android:id/btnApply").click()

    @teststep
    def click_google_login_img(self):
        log.i('点击google登录按钮')
        self.d(resourceId="com.vova.android:id/img_google").click()

    @teststep
    def click_facebook_login_img(self):
        log.i('点击facebook登录按钮')
        self.d(resourceId="com.vova.android:id/img_facebook").click()

    @staticmethod
    def login(username, password):
        login_page().input_username(username)
        time.sleep(.5)
        login_page().input_password(password)
        login_page().click_login_btn()
