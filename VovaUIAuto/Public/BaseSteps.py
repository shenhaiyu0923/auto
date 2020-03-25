#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest
from Public.ReadConfig import ReadConfig
from PageObject import home, login, user_center, search, commodity_details, account_setting, payment, country_list, \
    order_details, shipping_address, cards_list, checkout_v2, paypal, add_address_v2, welcome, edit_address, bag
from Public.Decorator import *
from Public.Test_data import get_test_data

a = BasePage().set_driver(None)
test_data = get_test_data(BasePage().d)


def creat_random_email():
    return ''.join(random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
         'e', 'd', 'c', 'b', 'a'], 10)) + '@tetx.com'


def init_app_operation():
    welcome.welcome_page().wait_page()
    welcome.welcome_page().select_gender('male')
    welcome.welcome_page().choose_age('31_to_45')
    home.home_page().click_account_button()
    user_center.user_page().wait_page()
    user_center.user_page().wait_get_it_gone()


def user_login(name, password):
    home.home_page().click_account_button()
    user_center.user_page().wait_page()
    user_center.user_page().wait_get_it_gone()
    user_center.user_page().click_signin_button()
    login.login_page().wait_page()
    BasePage.set_fastinput_ime()
    login.login_page().input_username(name)
    login.login_page().input_password(password)
    login.login_page().click_login_btn()
    user_center.user_page().discover_user_name()
    user_center.user_page().wait_is_login_page()


def user_register():
    home.home_page().click_account_button()
    user_center.user_page().wait_page()
    user_center.user_page().wait_get_it_gone()
    user_center.user_page().click_signin_button()

    login.login_page().wait_page()
    login.login_page().click_register_btn()
    BasePage.set_fastinput_ime()
    login.login_page().input_first_name(test_data['first_name'])
    login.login_page().input_last_name(test_data['last_name'])
    login.login_page().input_email(creat_random_email())
    login.login_page().input_register_password(test_data['register_password'])
    login.login_page().input_confirm_register_password(test_data['register_password'])
    login.login_page().click_login_btn()
    home.home_page().click_home_button()


def user_logout():
    home.home_page().wait_page()
    home.home_page().click_account_button()

    user_center.user_page().wait_page()
    user_center.user_page().click_setting_button()

    account_setting.account_setting_page().wait_page()
    account_setting.account_setting_page().click_sign_out_button()


def search_goods_by_id(goods_id, index=0):
    home.home_page().click_search_button()
    search.search_page().wait_page()
    search.search_page().click_search_box()
    search.search_page().wait_search_inner_page()
    search.search_page().click_inner_search_box()
    search.search_page().input_goods_id_to_search(goods_id)
    search.search_page().wait_goods_img()
    search.search_page().click_item_img(index=index)


def buy_goods_with_attr(attrs=None, add_num=0, del_num=0):
    commodity_details.commodity_details_page().wait_page()
    commodity_details.commodity_details_page().click_bag_button()
    if attrs:
        for attr in attrs:
            commodity_details.commodity_details_page().select_goods_attr(attr)
        for i in range(add_num):
            commodity_details.commodity_details_page().click_add_amount_button()
        for j in range(del_num):
            commodity_details.commodity_details_page().click_reduce_amount_button()
        commodity_details.commodity_details_page().click_add_to_bag_button()
    bag.bag_page().wait_page()


def buy_goods_with_attr_by_cod(attrs):
    commodity_details.commodity_details_page().wait_page()
    commodity_details.commodity_details_page().click_bag_button()
    for attr in attrs:
        commodity_details.commodity_details_page().select_goods_attr(attr)
    commodity_details.commodity_details_page().click_add_to_bag_button()
    bag.bag_page().wait_page()
    while not bag.bag_page().is_cod():
        commodity_details.commodity_details_page().click_add_amount_button()
        time.sleep(0.5)


def checkout_without_coupon():
    bag.bag_page().wait_page()
    if bag.bag_page().is_use_coupon():
        bag.bag_page().click_coupon_chose_button()
        bag.bag_page().click_no_use_coupon_button()
        bag.bag_page().wait_page()
    bag.bag_page().click_checkout_button()
    checkout_v2.checkout_page().wait_page()


def add_shipping_address_in_order(text=''):
    add_address_v2.add_address_page().wait_add_page()
    add_address_v2.add_address_page().input_first_name(test_data['first_name'])
    add_address_v2.add_address_page().input_last_name(test_data['last_name'])
    add_address_v2.add_address_page().input_phone(test_data['phone'])

    if add_address_v2.add_address_page().is_email_exists():  # 订单转移case用，so先写死转移用户
        add_address_v2.add_address_page().input_email(test_data['user_name_02'])

    add_address_v2.add_address_page().input_address(test_data['detail_address']+text)
    add_address_v2.add_address_page().input_state(test_data['state'])
    add_address_v2.add_address_page().input_city(test_data['city'])
    add_address_v2.add_address_page().input_zip_code(test_data['zip_code'])
    # add_address_v2.add_address_page().click_default_address_button()
    # add_address_v2.add_address_page().click_default_billing_button()
    add_address_v2.add_address_page().click_save_button()
    checkout_v2.checkout_page().wait_page()


def add_address_in_setting():
    home.home_page().wait_page()
    home.home_page().click_account_button()
    user_center.user_page().wait_page()
    user_center.user_page().click_setting_button()
    account_setting.account_setting_page().wait_page()
    account_setting.account_setting_page().open_address_list()
    shipping_address.shipping_address_page().wait_page()

    # 判断是否第一次加地址
    if shipping_address.shipping_address_page().is_first_add_address_button():
        log.i('首次新增')
        shipping_address.shipping_address_page().click_add_first_address_button()
    else:
        log.i('非首次新增')
        shipping_address.shipping_address_page().click_setting_add_address_button()

    add_address_v2.add_address_page().wait_add_page()
    add_address_v2.add_address_page().input_first_name(test_data['first_name'])
    add_address_v2.add_address_page().input_last_name(test_data['last_name'])
    add_address_v2.add_address_page().input_phone(test_data['phone'])

    add_address_v2.add_address_page().input_state(test_data['state'])
    add_address_v2.add_address_page().input_city(test_data['city'])
    add_address_v2.add_address_page().input_address(test_data['detail_address'])
    add_address_v2.add_address_page().input_zip_code(test_data['zip_code'])

    add_address_v2.add_address_page().click_default_address_button()
    add_address_v2.add_address_page().click_default_billing_button()
    add_address_v2.add_address_page().click_save_button()


def ensure_needed_country_and_address(country_name):
    # country
    if checkout_v2.checkout_page().get_current_country() != country_name:
        checkout_v2.checkout_page().click_change_country()
        country_list.country_list_page().wait_page()
        country_list.country_list_page().search_country(country_name)
        country_list.country_list_page().select_country(country_name)
        country_list.country_list_page().ensure_country()
        checkout_v2.checkout_page().wait_page()
    # address
    if checkout_v2.checkout_page().is_exists_default_address(country_name) is False:
        checkout_v2.checkout_page().click_add_shipping_address_in_order()
        add_shipping_address_in_order()


def one_step_to_checkout_without_coupon(country_name, goods_id, attrs, index=0):
    """
        one_step_to_checkout
        :param == one_step_to_pay ↓↓↓
    """
    search_goods_by_id(goods_id, index=index)
    if country_name == 'Austria':
        buy_goods_with_attr(attrs, add_num=int(test_data['cod_num']), del_num=1)
    else:
        buy_goods_with_attr(attrs)
    if bag.bag_page().is_use_coupon():
        bag.bag_page().click_coupon_chose_button()
        bag.bag_page().wait_coupons_page()
        bag.bag_page().click_no_use_coupon_button()
        bag.bag_page().wait_page()
    bag.bag_page().click_checkout_button()
    checkout_v2.checkout_page().wait_page()


def one_step_to_checkout_with_needed_coupon(goods_id, attrs, index=0):
    """
        one_step_to_checkout_with_needed_coupon
        :param == one_step_to_pay ↓↓↓
    """
    search_goods_by_id(goods_id, index=index)
    buy_goods_with_attr(attrs)
    bag.bag_page().click_coupon_chose_button()
    bag.bag_page().wait_coupons_page()
    bag.bag_page().chose_needed_coupon_button(test_data['coupon_discount'])
    bag.bag_page().wait_page()
    bag.bag_page().click_checkout_button()
    checkout_v2.checkout_page().wait_page()


def checkout_to_change_payment_method(p_method):
    checkout_v2.checkout_page().click_place_order_button()
    payment.payment_page().wait_page()
    payment.payment_page().change_payment_method(p_method)


def order_detail_to_change_payment_method(p_method):
    order_details.order_details_page().click_pay_button_v2()
    payment.payment_page().wait_page()
    payment.payment_page().change_payment_method(p_method)


def one_step_to_pay(country_name, goods_id, attrs, p_method, index=0):
    """
        one_step_to_pay: 'Credit' or 'PayPal' need coupon
        :param country_name: init country support payment
        :param goods_id: support country , some goods_id id forbidden to some country
        :param attrs: map goods_id's attrs
        :param p_method payment_method
        :param index search_results num
        :return: None
    """
    if p_method == 'Credit' or p_method == 'PayPal':
        one_step_to_checkout_with_needed_coupon(goods_id, attrs, index=index)
    else:
        one_step_to_checkout_without_coupon(country_name, goods_id, attrs, index=index)
    ensure_needed_country_and_address(country_name)

    if country_name == 'Kuwait':
        checkout_v2.checkout_page().click_place_order_button()
    else:
        checkout_to_change_payment_method(p_method)


def order_detail_change_address(address):
    order_details.order_details_page().click_edit_address_button()
    edit_address.edit_address_page().input_address(address)
    edit_address.edit_address_page().click_save_button()
    order_details.order_details_page().wait_page()


def step_to_open_address_list():
    home.home_page().click_account_button()
    user_center.user_page().wait_page()
    user_center.user_page().click_setting_button()
    account_setting.account_setting_page().wait_page()
    account_setting.account_setting_page().open_address_list()


def go_shipping_address_edit_page(country_name):
    step_to_open_address_list()
    if shipping_address.shipping_address_page().is_exists_current_country_address(country_name):
        shipping_address.shipping_address_page().click_edit_button_for_address_v2()
        add_address_v2.add_address_page().wait_edit_page()


def del_all_address(country_name):
    BasePage().press_back_to_home()
    step_to_open_address_list()
    while shipping_address.shipping_address_page().is_exists_current_country_address(country_name):
        shipping_address.shipping_address_page().click_edit_button_for_address_v2()
        add_address_v2.add_address_page().wait_edit_page()
        add_address_v2.add_address_page().click_del_button_for_address_v2()
        # shipping_address.shipping_address_page().wait_page()  # 先不要
        time.sleep(5)  # 兼容刷新完成状态
    BasePage().press_back_to_home()


def del_all_cards():
    user_center.user_page().click_setting_button()
    account_setting.account_setting_page().wait_page()
    account_setting.account_setting_page().open_cards_list()
    cards_list.cards_list_page().wait_page()
    while cards_list.cards_list_page().is_card_exists() is False:
        cards_list.cards_list_page().click_card()
        cards_list.cards_list_page().wait_delete_button()
        cards_list.cards_list_page().click_delete_button()
        cards_list.cards_list_page().wait_card_miss()
    BasePage().press_back_to_home()


def del_all_address_and_cards(country_name):
    del_all_address(country_name)
    del_all_cards()


def change_country(country_name, goods_id, attrs, index=0):
    one_step_to_checkout_without_coupon(country_name, goods_id, attrs, index)
    ensure_needed_country_and_address(country_name)
    BasePage().press_back_to_home()


def empty_shopping_bag():
    home.home_page().click_bag_button()
    while bag.bag_page().is_empty_bag() is False:
        bag.bag_page().wait_page()
        bag.bag_page().long_click_goods_name()
        bag.bag_page().wait_delete_button()
        bag.bag_page().click_delete_button()
        bag.bag_page().wait_empty_status()
