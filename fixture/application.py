from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def  __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

        def test_add_pozov(self):
            success = True
            wd = self.wd
            # open home page
            wd.get("http://10.100.7.71:57775/osop/LoginForm.csp")
            # login
            wd.find_element_by_name("username").click()
            wd.find_element_by_name("username").click()
            wd.find_element_by_name("username").clear()
            wd.find_element_by_name("username").send_keys("test17")
            wd.find_element_by_name("password").click()
            wd.find_element_by_name("password").clear()
            wd.find_element_by_name("password").send_keys("bMS")
            wd.find_element_by_name("password").click()
            wd.find_element_by_name("password").clear()
            wd.find_element_by_name("password").send_keys("bMS$2016")
            wd.find_element_by_css_selector("input.btn.btn-primary").click()
            wd.find_element_by_id("button-1015-btnInnerEl").click()
            wd.find_element_by_id("menuitem-1017-textEl").click()
            wd.find_element_by_id("menuitem-1044-textEl").click()
            wd.find_element_by_id("button-1087-btnInnerEl").click()
            wd.find_element_by_id("combo-1195-trigger-picker").click()
            wd.find_element_by_id("ext-element-16").click()
            wd.find_element_by_id("combo-1196-trigger-picker").click()
            wd.find_element_by_id("ext-element-17").click()
            wd.find_element_by_id("treecombo-1199-trigger-picker").click()
            wd.find_element_by_xpath("//table[@id='treeview-1203-record-92']//span[.='З інших питань']").click()
            wd.find_element_by_xpath("//table[@id='treeview-1203-record-91']/tbody/tr/td/div/span").click()
            wd.find_element_by_id("textfield-1215-inputEl").click()
            wd.find_element_by_id("textfield-1215-inputEl").clear()
            wd.find_element_by_id("textfield-1215-inputEl").send_keys("1")
            wd.find_element_by_id("textfield-1216-inputEl").click()
            wd.find_element_by_id("textfield-1216-inputEl").clear()
            wd.find_element_by_id("textfield-1216-inputEl").send_keys("2")
            wd.find_element_by_id("button-1302-btnInnerEl").click()
            wd.find_element_by_id("button-1005-btnInnerEl").click()
            wd.find_element_by_id("button-1038-btnInnerEl").click()
            wd.find_element_by_id("button-1006-btnInnerEl").click()
            self.assertTrue(success)

    def_destroy (self):
        self.wd.quit()