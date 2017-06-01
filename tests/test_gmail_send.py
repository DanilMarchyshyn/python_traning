# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class gmail_send(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_gmail_send(self):
        success = True
        wd = self.wd
        wd.get("https://www.google.com/gmail/about/")
        wd.find_element_by_link_text("Увійти").click()
        wd.find_element_by_id("identifierId").click()
        wd.find_element_by_xpath("//div[@class='z0']//div[.='НАПИСАТЬ']").click()
        wd.find_element_by_id(":o4").click()
        wd.find_element_by_id(":o4").send_keys("\\68")
        wd.find_element_by_css_selector("div.Sr").click()
        wd.find_element_by_id(":no").click()
        wd.find_element_by_id(":no").clear()
        wd.find_element_by_id(":no").send_keys("test2")
        wd.find_element_by_id(":ne").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
