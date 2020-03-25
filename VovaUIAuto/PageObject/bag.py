#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class bag_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/title_text", text="Bag").wait(timeout=15):
                pass
            else:
                raise Exception('Not in BagPage')
        except Exception:
            raise Exception('Not in BagPage')

    @teststep
    def wait_coupons_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/tv_not_select_coupon").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Coupons Page')
        except Exception:
            raise Exception('Not in Coupons Page')

    @teststep
    def wait_checkout_button(self):
        try:
            if self.d(resourceId="com.vova.android:id/tv_not_select_coupon").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Coupons Page')
        except Exception:
            raise Exception('Not in Coupons Page')

    @teststep
    def wait_delete_button(self):
        try:
            if self.d(resourceId="com.vova.android:id/icon").wait(timeout=15):
                pass
            else:
                raise Exception('Not discover move')
        except Exception:
            raise Exception('Not discover move')

    @teststep
    def click_delete_button(self):
        self.d(resourceId="com.vova.android:id/icon")[1].click()
        log.i("点击移除购物车按钮")

    @teststep
    def click_checkout_button(self):
        self.d(resourceId="com.vova.android:id/buy_root").click()
        log.i("点击CheckOut按钮")

    @teststep
    def is_use_coupon(self):
        log.i('判断是否有用优惠券...')  # ture:用了  false:包括无优惠券+没用
        if self.element_is_exists(
            self.d(resourceId='com.vova.android:id/usecoupon', textContains='-')
        ):
            return True
        else:
            return False

    def is_cod(self):
        target = "Qualify for Free Shipping"
        return self.d(resourceId="com.vova.android:id/mideast_shipping_tv").get_text() == target

    @teststep
    def click_coupon_chose_button(self):
        self.d(resourceId="com.vova.android:id/all_jump_img").click()
        log.i("点击优惠券选择按钮")

    @teststep
    def click_no_use_coupon_button(self):
        self.d(resourceId="com.vova.android:id/tv_not_select_coupon").sibling(
            resourceId='com.vova.android:id/view_checker').click()
        log.i("点击do not use优惠券按钮")

    @teststep
    def click_needed_coupon_button(self):
        self.d(resourceId="com.vova.android:id/tv_not_select_coupon").sibling(
            resourceId='com.vova.android:id/view_checker').click()
        log.i("点击do not use优惠券按钮")

    @teststep
    def chose_needed_coupon_button(self, coup_text):
        time.sleep(.5)  # 先点出coup选择框，再滑动，兼容选择框未完全出来，就滑动，导致选择框刚出立即消失
        self.find_element_by_swipe_up(
            self.d(resourceId="com.vova.android:id/coupon_title", textContains=coup_text),
            element=self.d(resourceId='com.vova.android:id/rv_coupons'), max_swipe=5)
        self.d(resourceId="com.vova.android:id/coupon_title", textContains=coup_text).left(
            resourceId='com.vova.android:id/view_checker').click_exists()
        log.i("选择%s优惠券按钮" % coup_text)

    @teststep
    def long_click_goods_name(self):
        self.d(resourceId="com.vova.android:id/goods_name").long_click()
        log.i("长按购物车商品")

    @teststep
    def is_empty_bag(self):
        return self.d(text="You Might Like").exists(timeout=3)

    @teststep
    def wait_empty_status(self):
        self.d(text="You Might Like").wait(timeout=1.0)
