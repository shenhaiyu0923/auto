#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class payment_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/pay_title_tv", textContains='Credit').wait(timeout=25):
                time.sleep(.5)  # 兼容页面加载，安卓每次进来页面都刷新一下，麻烦
            else:
                raise Exception('Not in PaymentPage')
        except Exception:
            raise Exception('Not in PaymentPage')

    @teststep
    def wait_payment_methods(self):
        try:
            if self.d(resourceId="com.vova.android:id/imageView_logo").wait(timeout=15):
                pass
            else:
                raise Exception('Not discover payment methods')
        except Exception:
            raise Exception('Not discover payment methods')

    @teststep
    def click_pay_button(self):
        self.d(resourceId="com.vova.android:id/normal_buy_btn").click_exists(timeout=3.0)
        log.i("点击确认付款按钮")

    @teststep
    def click_payment_methods(self):
        self.d(resourceId="com.vova.android:id/imageView_logo").click_exists(timeout=3.0)
        log.i("选择当前支付方式")

    @teststep
    def click_ideal_pay(self):
        self.d(resourceId="com.vova.android:id/button_confirm").click_exists(timeout=3.0)
        log.i("选择当前支付方式")

    @teststep
    def change_payment_method(self, method):
        a = self.d(resourceId="com.vova.android:id/pay_title_tv", textContains=method).sibling(
            resourceId="com.vova.android:id/payment_info_sel")
        if 'Credit' in method:
            if self.element_is_exists(self.d(resourceId="com.vova.android:id/credit_card_img")[1], timeout=4):
                self.d(resourceId="com.vova.android:id/credit_card_img")[0].sibling(
                    className="android.widget.ImageView").click(timeout=2)
                log.i("成功选择付款方式：%s, 已选择第一张信用卡" % method)
            else:
                a.click(timeout=3)
                log.i("成功选择付款方式：%s, 暂无信用卡" % method)
        else:
            if self.element_is_exists(a) is False:
                self.find_element_by_swipe_up(a)
            a.click(timeout=3)
            log.i("成功选择付款方式：%s" % method)

    @teststep
    def input_card_number(self, text):
        log.i("输入信用卡号：" + text)
        self.d(resourceId="com.vova.android:id/card_number_edit").set_text(text)

    @teststep
    def input_expiry_date(self):
        log.i("选择信用卡到期日")
        self.d(resourceId="com.vova.android:id/expire_date_jump_img").click()
        self.d(resourceId="com.vova.android:id/btnApply").click_exists(timeout=1.0)

    @teststep
    def input_cvv(self, text):
        log.i("输入信用卡cvv号：" + text)
        self.d(resourceId="com.vova.android:id/cvv_edit_text").set_text(text)

    @teststep
    def chose_first_card(self):
        self.d(resourceId="com.vova.android:id/credit_card_img")[0].sibling(
            className="android.widget.ImageView").click(timeout=2)
        log.i("成功选择第一张卡")

    @teststep
    def input_pay_code(self, payment_method, text):
        a = self.d(resourceId="com.vova.android:id/pay_title_tv", text=payment_method).sibling(
            className="android.widget.EditText")
        a.clear_text()
        a.set_text(text)
        self.set_original_ime()  # 兼容底部ime輸入法覆蓋掉底部button
        log.i("%s_code:%s输入完成" % (payment_method, text))

    @teststep
    def click_confirm_to_pay(self):
        self.d(resourceId="com.vova.android:id/normal_buy_btn").click()
        log.i("点击confirm to pay")

    @teststep
    def swipe_to_pay(self):
        a = self.d(resourceId="com.vova.android:id/slide_checkout_button").info
        xs = a['bounds']['left'] + 1
        ys = a['bounds']['top'] + 1
        xe = a['bounds']['right'] - 1
        ye = a['bounds']['top'] + 1
        self.d.swipe_ext("right", box=(xs, ys, xe, ye))
        log.i("滑动完成，等待支付成功状态返回..")

    @teststep
    def wait_card_list_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/credit_select_tv", text='CREDIT CARD LIST').wait(timeout=15):
                pass
            else:
                raise Exception('Not in PaymentPage')
        except Exception:
            raise Exception('Not in PaymentPage')

    @teststep
    def wait_confirm_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text='Confirmation').wait(timeout=15):
                pass
            else:
                raise Exception('Not in PaymentPage')
        except Exception:
            raise Exception('Not in PaymentPage')
        log.i('成功进入confirmation页面')

    @teststep
    def click_confirm_shop_now(self):
        self.d(resourceId="com.vova.android:id/try_again_btn", text='SHOP NOW').click()
        log.i("点击SHOP NOW")

    @teststep
    def click_add_a_card(self):
        self.d(text='Add a Card').click()
        log.i("点击Add a Card")