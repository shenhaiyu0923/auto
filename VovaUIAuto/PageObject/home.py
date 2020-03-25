#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class home_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/rv_nav_home_plates").wait(timeout=15):
                pass
            else:
                raise Exception('Not in HomePage')
        except Exception:
            raise Exception('Not in HomePage')

    @teststep
    def click_account_button(self):
        self.d(resourceId="com.vova.android:id/account_container").click()
        log.i("点击用户中心按钮")

    @teststep
    def click_search_button(self):
        self.d(resourceId="com.vova.android:id/search_container").click()
        log.i("点击搜索按钮")

    @teststep
    def click_top_search(self):
        self.d(resourceId="com.vova.android:id/search_layout").click()
        log.i("点击顶部搜索框")

    @teststep
    def click_home_button(self):
        self.d(resourceId="com.vova.android:id/home_container").click()
        log.i("点击首页按钮")

    @teststep
    def click_bag_button(self):
        self.d(resourceId="com.vova.android:id/cart_container").click()
        log.i("点击购物车按钮")

    # @teststep
    # def click_tab(self, inst=1):
    #     '''
    #     点击底部tab
    #     :param inst: tab的位数
    #     :return:
    #     '''
    #     ele = self.d(resourceId="android:id/tabs").child(className="android.widget.LinearLayout", instance=inst-1)
    #     text = ele.child(resourceId="com.github.android_app_bootstrap:id/textview").get_text()
    #     ele.child(resourceId="com.github.android_app_bootstrap:id/imageview").click()
    #     log.i('点击Tab %s' % text)
    #
    # @teststep
    # def click_list_btn(self):
    #     log.i('点击list按钮')
    #     self.d(resourceId="com.github.android_app_bootstrap:id/list_button").click()
    #
    # @teststep
    # def click_logout_btn(self):
    #     log.i('点击退出按钮')
    #     self.d(resourceId="com.github.android_app_bootstrap:id/logout_button").click()


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # log.i(creation_page().click_view_pager_btn('素材中心'))
    home_page().click_tab(2)
