#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os


proDir = os.path.split(os.path.realpath(__file__))[0]
# 将path分割成路径名和文件名
configPath = os.path.join(proDir, "config.ini")
# 将多个路径组合后返回


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='UTF-8')

    def get_method(self):
        value = self.cf.get("DEVICES", 'method')
        return value

    def get_server_url(self):
        value = self.cf.get("DEVICES", "server")
        return value

    def get_server_token(self):
        value = self.cf.get("DEVICES", "token")
        return value

    def get_server_udid(self):
        value = self.cf.get("DEVICES", "udid")
        return value.split('|')

    def get_devices_ip(self):
        value = self.cf.get("DEVICES", "IP")
        return value.split('|')

    def get_apk_url(self):
        value = self.cf.get("APP", "apk_url")
        return value

    def get_apk_path(self, env):
        value = self.cf.get("APP", env + "_apk_path")
        return value

    def get_pkg_name(self):
        value = self.cf.get("APP", "pkg_name")
        return value

    def get_testdata(self, env, name):
        value = self.cf.get(env, name)
        a = value.split('|')
        return a

    def get_test_env(self):
        value = self.cf.get("TESTENV", "test_environment")
        return value

    def get_all_option(self, section):
        return self.cf.options(section)


if __name__ == '__main__':
    env = "TESTDATA"
    print(ReadConfig().get_all_option(env))

    dict_tmp = {}
    for i in ReadConfig().get_all_option(env):
        dict_tmp[i] = ReadConfig().get_testdata(env, i)

    print(dict_tmp)

