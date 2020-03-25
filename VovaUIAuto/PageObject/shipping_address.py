#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class shipping_address_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(className='android.widget.TextView', textStartsWith='A').wait(timeout=15):
                log.i(self.d(className='android.widget.TextView', textStartsWith='A').get_text())
            else:
                raise Exception('Not in ShippingAddressPage')
        except Exception:
            raise Exception('Not in ShippingAddressPage')

    @teststep
    def wait_flush_gone(self, element=None):
        return element.count

    @teststep
    def is_first_add_address_button(self):
        log.i('判断是否首次新增地址...')
        return self.element_is_exists(
            self.d(resourceId='com.vova.android:id/fav_show_now_btn')
        )

    @teststep
    def click_add_first_address_button(self):
        self.d(resourceId="com.vova.android:id/fav_show_now_btn").click()
        log.i("点击Add Address按钮")

    @teststep
    def click_setting_add_address_button(self):
        self.d(resourceId="com.vova.android:id/rightTv").click()
        log.i("点击Add Address按钮")

    @teststep
    def select_default_address(self, text):
        self.find_element_by_swipe_up(self.d(resourceId="com.vova.android:id/address", text=text), max_swipe=10)
        time.sleep(1.0)
        self.d(resourceId="com.vova.android:id/address", text=text).click_exists()

    @teststep
    def select_needed_address_with_text_and_index(self, text, index=1):
        self.d(resourceId="com.vova.android:id/countryDesTv", textContains=text)[index].click(timeout=3)
        log.i("成功选择另一个地址")

    @teststep
    def select_needed_address_with_text(self, text):
        self.find_element_by_swipe_up(self.d(
            resourceId="com.vova.android:id/countryDesTv", textContains=text), max_swipe=10).click_exists(timeout=5)

    @teststep
    def click_menu_button_for_address(self):
        self.d(resourceId="com.vova.android:id/iv_more").click()
        log.i("打开地址操作菜单")

    @teststep
    def click_edit_button_for_address(self):
        self.d(resourceId="com.vova.android:id/tv_text", text="Edit").click()
        log.i("点击编辑地址按钮")

    @teststep
    def is_exists_current_country_address(self, country_name):
        if BasePage.element_is_exists(
                self.d(resourceId="com.vova.android:id/countryDesTv", textContains=country_name), timeout=0) is False:
            try:
                self.find_element_by_swipe_up(
                    self.d(resourceId="com.vova.android:id/countryDesTv", textContains=country_name), max_swipe=4)
            except UiObjectNotFoundError:
                return False
            return BasePage.element_is_exists(
                self.d(resourceId="com.vova.android:id/countryDesTv", textContains=country_name), timeout=0)
        else:
            return True

    @teststep
    def click_edit_button_for_address_v2(self):
        self.d(resourceId="com.vova.android:id/addressModifyIv")[0].click()
        log.i("选择第一个地址,点击编辑按钮")

    @teststep
    def get_edit_addree_des(self, country_name):
        return self.d(resourceId="com.vova.android:id/countryDesTv", textContains=country_name)[0].get_text

    @teststep
    def click_del_button_for_address(self):
        self.d(resourceId="com.vova.android:id/tv_text", text="Delete").click()
        log.i("点击删除地址按钮")

    @teststep
    def wait_be_del_address_gone(self, address):
        self.d(text=address).wait_gone(timeout=2.0)

