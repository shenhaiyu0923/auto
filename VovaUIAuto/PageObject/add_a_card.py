#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError
import datetime


class add_card_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text='Add a Card').wait(timeout=15):
                pass
            else:
                raise Exception('Not in Add a Card')
        except Exception:
            raise Exception('Not in Add a Card')

    @teststep
    def input_card_number(self, text):
        log.i("输入信用卡号：%s" % text)
        self.d(resourceId="com.vova.android:id/card_number_edit").set_text(text)

    @teststep
    def input_card_date(self, date):
        log.i("选择信用卡到期日")
        self.d(resourceId="com.vova.android:id/expire_date_tv").set_text(date)

    @teststep
    def click_chose_date(self):
        log.i("点击进行日期选择")
        self.d(resourceId="com.vova.android:id/iv_arrow").click()

    @teststep
    def swipe_to_chose_month(self, month):
        t = int(month) - datetime.datetime.now().month
        a = self.d(resourceId="com.vova.android:id/month").info
        xs = a['bounds']['left'] + 1
        ys = a['bounds']['top'] + 1
        xe = a['bounds']['right'] - 1
        ye = a['bounds']['top'] + 0.2 * (a['bounds']['bottom'] - a['bounds']['top'])
        if t >= 0:
            while t:
                self.d.swipe_ext("up", box=(xs, ys, xe, ye))
                t -= 1
                time.sleep(.5)
        else:
            while t:
                self.d.swipe_ext("down", box=(xs, ys, xe, ye))
                t += 1
                time.sleep(.5)
        log.i("成功选择月份%s" % month)

    @teststep
    def swipe_to_chose_year(self, year):
        t = int(year) - datetime.datetime.now().year
        a = self.d(resourceId="com.vova.android:id/year").info
        xs = a['bounds']['left'] + 1
        ys = a['bounds']['top'] + 1
        xe = a['bounds']['right'] - 1
        ye = a['bounds']['top'] + 0.2 * (a['bounds']['bottom'] - a['bounds']['top'])
        while t:
            self.d.swipe_ext("up", box=(xs, ys, xe, ye))
            # self.d.swipe_ext("up", box=(540, 1585, 1080, 1700))
            t -= 1
            time.sleep(.5)
        log.i("成功选择年份%s" % year)

    @teststep
    def click_date_confirm(self):
        log.i("提交银行卡选择日期")
        self.d(resourceId="com.vova.android:id/btnApply", text='Confirm').click()

    @teststep
    def input_expiry_date(self):
        log.i("选择信用卡到期日")
        self.d(resourceId="com.vova.android:id/expire_date_jump_img").click()
        self.d(resourceId="com.vova.android:id/btnApply").click_exists(timeout=1.0)

    @teststep
    def input_card_cvv(self, text):
        log.i("输入信用卡cvv号：%s" % text)

        self.d(resourceId="com.vova.android:id/cvv_edit_text").set_text(text)

    @teststep
    def click_use_card(self):
        log.i("点击use this card")
        self.d(resourceId="com.vova.android:id/pay_btn").click()

    @teststep
    def click_pay_button(self):
        self.d(resourceId="com.vova.android:id/normal_buy_btn").click_exists(timeout=3.0)
        log.i("点击确认付款按钮")

    @teststep
    def change_payment_method(self, method):
        a = self.d(resourceId="com.vova.android:id/pay_title_tv", textContains=method).sibling(
                className="android.widget.ImageView")
        a[2].click(timeout=2) if 'Boleto' in method else a[1].click(timeout=2)
        log.i("成功选择付款方式：" + method)

    @teststep
    def chose_first_card(self):
        self.d(resourceId="com.vova.android:id/credit_card_img")[0].sibling(
            className="android.widget.ImageView").click(timeout=2)
        log.i("成功选择第一张卡")
