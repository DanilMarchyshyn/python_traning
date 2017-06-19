# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class add_pozov(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_hpme_pages(self, wd):
        wd.get("http://10.100.7.71:57775/osop/LoginForm.csp")

    def login(self, wd, username, password):
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("%s" % password)
        wd.find_element_by_css_selector("input.btn.btn-primary").click()

    def test_add_pozov(self):
        success = True
        wd = self.wd
        self.open_hpme_pages(wd)
        self.login(wd, username="test17", password="bMS$2016")
        # open groups page
        wd.find_element_by_id("button-1015-btnInnerEl").click()
        wd.find_element_by_id("menuitem-1027-itemEl").click()
        wd.find_element_by_id("button-1062-btnInnerEl").click()
        wd.find_element_by_id("datefield-1178-trigger-picker").click()
        wd.find_element_by_xpath("//td[@id='datepicker-1197-cell-30']//div[.='31']").click()
        wd.find_element_by_id("treecombo-1179-trigger-picker").click()
        wd.find_element_by_xpath("//table[@id='treeview-1183-record-124']//span[.='Інформація в органи влади']").click()
        wd.find_element_by_id("textfield-1188-inputEl").click()
        wd.find_element_by_id("textfield-1188-inputEl").clear()
        wd.find_element_by_id("textfield-1188-inputEl").send_keys("1")
        wd.find_element_by_id("textfield-1189-inputEl").click()
        wd.find_element_by_id("textfield-1189-inputEl").clear()
        wd.find_element_by_id("textfield-1189-inputEl").send_keys("2")
        wd.find_element_by_id("button-1195-btnInnerEl").click()
        wd.find_element_by_id("button-1005-btnInnerEl").click()
        wd.find_element_by_id("button-1038-btnInnerEl").click()
        wd.find_element_by_id("button-1006-btnInnerEl").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

