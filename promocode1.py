# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class promocode1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_promocode1(self):
        success = True
        wd = self.wd
        wd.get("https://go.solomoto.com/spa/")
        wd.find_element_by_xpath("//div[@class='loginForm__tabsContainer__tabsWrapper']//div[.='log in']").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("kolbassa@inbox.ru")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("1234567")
        wd.find_element_by_xpath("//div[@class='loginForm__tabsContainer__tabsWrapper']/div[3]/form[1]/input").click()
        wd.find_element_by_link_text("!S_PXTSST").click()
        wd.find_element_by_link_text("!S_qwerty").click()
        wd.find_element_by_link_text("BALANCE
                $0.00").click()
        wd.find_element_by_xpath("//div[1]").click()
        wd.find_element_by_xpath("//div[@class='balance-promocode__container']/form/div/div/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='balance-promocode__container']/form/div/div/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='balance-promocode__container']/form/div/div/div[2]/input").send_keys("1337-solomoto-test")
        wd.find_element_by_css_selector("button.balance-submit-button.ng-binding").click()
        wd.find_element_by_xpath("//div[@class='modal-content']//button[normalize-space(.)='OK']").click()
        wd.find_element_by_xpath("//div[@id='solomoto-app']//span[.='Payment history']").click()
        wd.find_element_by_xpath("//header[@class='header']/div[2]/div[8]/div/a/img").click()
        wd.find_element_by_xpath("//header[@class='header']//button[.='Sign out']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
