#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from Public.BasePage import BasePage
# from Public.maxim_monkey import Maxim
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class search_page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.vova.android:id/tv_all").wait(timeout=15):
                pass
            else:
                raise Exception('Not in SearchPage')
        except Exception:
            raise Exception('Not in SearchPage')

    @teststep
    def click_search_box(self):
        a = 1
        if self.d(resourceId="com.vova.android:id/category_title").exists(timeout=1.0) is False:
            self.d(resourceId="com.vova.android:id/category_title").exists(timeout=6.0)
        while self.d(resourceId="com.vova.android:id/category_title").click_exists(timeout=3.0):
            if a == 1:
                log.i("点击搜索框")
            else:
                log.i("第%d次点击搜索框" % a)
            a += 1
            self.d(resourceId="com.vova.android:id/category_title").wait_gone(timeout=2.0)

    @teststep
    def wait_search_inner_page(self):
        self. wait_element_exists(self.d(resourceId="com.vova.android:id/icet_search"))
        log.i("成功进入内部搜索页")

    @teststep
    def click_inner_search_box(self):
        self.d(resourceId="com.vova.android:id/icet_search").click(timeout=2)
        log.i("点击内部搜索框")

    @teststep
    def input_goods_id_to_search(self, text):
        log.i('输入Goods ID:%s' % text)
        self.d(resourceId="com.vova.android:id/icet_search").set_text(text)
        self.d.send_action("search")

    @teststep
    def click_history_search(self, text):
        log.i('输入Goods ID:%s' % text)
        return self.d(resourceId="com.vova.android:id/search_history_container").\
            child_by_text(text, className="android.widget.TextView").click_exists(timeout=3.0)

    @teststep
    def wait_goods_img(self, max_times=3):
        for i in range(max_times):
            if not self.d(resourceId="com.vova.android:id/goods_card_view").exists(timeout=3.0):
                self.d(text="Try Again").click_exists(timeout=1)
                self.swipe_down()
            else:
                break

    @teststep
    def click_item_img(self, index=0):
        time.sleep(2)  # 兼容刷新状态下点击无效
        try:
            self.d(resourceId="com.vova.android:id/goods_card_view")[index].click(timeout=3.0)
        except UiObjectNotFoundError:
            self.swipe_down()
            time.sleep(2)  # 兼容刷新状态下点击无效
            self.d(resourceId="com.vova.android:id/goods_card_view")[index].click(timeout=5.0)
        log.i('点击搜索結果页商品图片')


if __name__ == '__main__':
    search_page.input_goods_id_to_search("123456")
