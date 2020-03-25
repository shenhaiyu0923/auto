#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uiautomator2 as u2
from Public import BaseSteps
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from Public.Test_data import get_test_data

apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()
test_apk_path = ReadConfig().get_apk_path("test")
pre_apk_path = ReadConfig().get_apk_path("pre")
test_env = ReadConfig().get_test_env()


# @unittest.skip
class apk_install(unittest.TestCase, BasePage):
    '''新装app'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_stop_all()
        cls.test_data = get_test_data(cls.d)
        cls.watch_device("GET IT!")

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.vova.android")

    @testcase
    def test_01_install_apk(self):
        '''安装启动android_app_vova'''
        self.d.app_uninstall(pkg_name)
        # self.d.app_install(apk_url)
        if test_env == "test":
            self.local_install(test_apk_path)
            log.i("成功安装测试包")
        elif test_env == "pre":
            self.local_install(pre_apk_path)
            log.i("成功安装release包")
        else:
            log.i("Wrong test environment")
            return
        self.d.app_start(pkg_name)
        BaseSteps.init_app_operation()
