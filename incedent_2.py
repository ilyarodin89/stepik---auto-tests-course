# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox() #("D:\\testcase\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://config-test-node1.sk.newdv/core/")
        login = driver.find_element_by_id("UserName")
        login.clear()
        login.send_keys("Rodin")
        pswd = driver.find_element_by_id("Password")
        pswd.clear()
        pswd.send_keys("!Rodin123")

        """
        #driver.find_element_by_id("UserName").click()
        #driver.find_element_by_id("UserName").clear()
        #driver.find_element_by_id("UserName").send_keys("BratskEDDS2")
        #driver.find_element_by_id("Password").click()
        #driver.find_element_by_id("Password").clear()
        #driver.find_element_by_id("Password").send_keys("BratskEDDS2!")"""
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Безопасный город'])[1]/following::button[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        #driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Моя страница'])[2]/following::span[5]").click()
        driver.find_element_by_name("filter")#.click()
        driver.find_element_by_name("filter").clear()
        driver.find_element_by_name("filter").send_keys("148")

        driver.find_element_by_name("filter").send_keys(Keys.ENTER)
        driver.find_element_by_link_text("148").click()

        time.sleep(20)



    """def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True"""
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)
        print("Close browser")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

