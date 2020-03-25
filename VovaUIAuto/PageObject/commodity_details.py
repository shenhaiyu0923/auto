#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class commodity_details_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/button_buy").wait(timeout=30):
                pass
            else:
                raise Exception('Not in GoodsDetailPage')
        except Exception:
            raise Exception('Not in GoodsDetailPage')

    @teststep
    def click_bag_button(self):
        self.d(resourceId="com.vova.android:id/button_buy").click()
        log.i("点击加购按钮")

    @teststep
    def click_go_coupons_button(self):
        self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/iv_go_coupon"))
        self.d(resourceId="com.vova.android:id/iv_go_coupon").click_exists(timeout=3.0)
        log.i("打开选择优惠券弹窗")

    @teststep
    def get_coupons(self, index=1):
        _xpath = '//*[@resource-id="com.vova.android:id/coupon_listview"]/android.widget.RelativeLayout[' \
                 + str(index) + ']/android.widget.RelativeLayout[1]/android.widget.TextView[1]'
        self.find_element_by_swipe_up(self.d.xpath(_xpath))
        self.d.xpath(_xpath).click()
        log.i("选择第" + str(index) + "张优惠券")

    @teststep
    def select_goods_attr(self, attr):
        self.d(resourceId="com.vova.android:id/element_item_textview", text=attr).click_exists(timeout=3.0)
        log.i("选择商品属性：" + attr)

    @teststep
    def click_add_to_bag_button(self):
        if self.d(resourceId="com.vova.android:id/tv_bottom_btn").info["enabled"]:
            self.d(resourceId="com.vova.android:id/tv_bottom_btn").click()
            log.i("选择完商品属性后点击确认购买按钮")
            # 先消失弹窗后消失页面
            self.d(resourceId="com.vova.android:id/tv_bottom_btn").wait_gone(timeout=5.0)
            self.d(resourceId="com.vova.android:id/button_buy").wait_gone(timeout=10.0)

            if self.d(resourceId="com.vova.android:id/button_buy").click_exists(timeout=1.0):
                log.i("二次点击确认购买按钮")  # 兼容低概率点上不跳转的bug
        else:
            log.i("商品属性未选择完成")

    @teststep
    def click_add_amount_button(self):
        self.d(resourceId="com.vova.android:id/btn_add").click()
        log.i("点击增加商品数量按钮")

    @teststep
    def click_reduce_amount_button(self):
        self.d(resourceId="com.vova.android:id/btn_sub").click()
        log.i("点击减少商品数量按钮")

    @teststep
    def click_more_attr_button(self):
        if BasePage.element_is_exists(self.d(resourceId="com.vova.android:id/tv_style_content"), timeout=0) is False:
            self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/tv_style_content"))
            time.sleep(1)
        self.d(resourceId="com.vova.android:id/tv_style_content").click()
        log.i("点击弹起商品属性选择弹窗")

    @teststep
    def chose_express_shipping(self):
        self.d(resourceId="com.vova.android:id/iv_select_fbv").click()
        log.i("选择海外仓方式")

    @teststep
    def wait_attr_pop_up(self):
        try:
            if self.d(resourceId="com.vova.android:id/tv_quantity").wait(timeout=4):
                pass
            else:
                raise Exception('Not discover pop-up')
        except Exception:
            raise Exception('Not discover pop-up')
