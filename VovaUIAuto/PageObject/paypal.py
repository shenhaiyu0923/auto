#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class paypal_sandbox_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="return_url", text='Proceed with Sandbox Purchase').wait(timeout=25):
                pass
            else:
                raise Exception('Not in paypal_page')
        except Exception:
            raise Exception('Not in paypal_page')

    @teststep
    def click_proceed_button(self):
        self.d(resourceId="return_url", text='Proceed with Sandbox Purchase').click_exists(timeout=3.0)
        log.i("点击确认沙盒支付")

    @teststep
    def change_payment_method(self, method):
        if self.d(resourceId="com.vova.android:id/pay_title_tv", text=method).sibling(
                className="android.widget.ImageView")[1].click_exists():
            log.i("成功选择付款方式：%s" % method)
        else:
            log.i("未找到指定的付款方式：%s" % method)

    @teststep
    def input_card_number(self, text):
        log.i("输入信用卡号：%s" % text)
        self.d(resourceId="com.vova.android:id/card_number_edit").set_text(text)

    @teststep
    def input_expiry_date(self):
        log.i("选择信用卡到期日")
        self.d(resourceId="com.vova.android:id/expire_date_jump_img").click()
        self.d(resourceId="com.vova.android:id/btnApply").click_exists(timeout=1.0)

    @teststep
    def input_cvv(self, text):
        log.i("输入信用卡cvv号：%s" % text)
        self.d(resourceId="com.vova.android:id/cvv_edit_text").set_text(text)

    @teststep
    def change_payment_method_v2(self, method):
        self.d(resourceId="com.vova.android:id/pay_title_tv", textContains=method).sibling(
            className="android.widget.ImageView")[1].click(timeout=2)
        log.i("成功选择付款方式：%s" % method)

    @teststep
    def change_special_payment_method(self, method):
        self.d(resourceId="com.vova.android:id/pay_title_tv", textContains=method).sibling(
            className="android.widget.ImageView")[2].click(timeout=2)
        log.i("成功选择付款方式：%s" % method)

    @teststep
    def chose_first_card(self):
        self.d(resourceId="com.vova.android:id/credit_card_img")[0].sibling(
            className="android.widget.ImageView").click(timeout=2)
        log.i("成功选择第一张卡")

    @teststep
    def input_boleto_code(self, text):
        a = self.d(resourceId="com.vova.android:id/pay_title_tv", text='Boleto').sibling(
            className="android.widget.EditText")
        a.clear_text()
        a.set_text(text)
        self.set_original_ime()  # 兼容底部ime輸入法覆蓋掉底部button
        log.i('boleto_code：%s输入完成' % text)

    @teststep
    def click_confirm_to_pay(self):
        self.d(resourceId="com.vova.android:id/normal_buy_btn", text='Confirm to Pay').click()
        log.i("点击confirm to pay")

    @teststep
    def wait_card_list_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/credit_select_tv", text='CREDIT CARD LIST').wait(timeout=15):
                pass
            else:
                raise Exception('Not in PaymentPage')
        except Exception:
            raise Exception('Not in PaymentPage')
