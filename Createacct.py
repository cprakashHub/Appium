import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from time import sleep
from Findpath import Findpat
from Locvalues import values
from Locvalues import home
from Locvalues import invalid

class welcreate(Findpat):

    def __init__(self, driver):
      super().__init__(driver)
      self.driver = driver

    def invalid(self):
        inv = Findpat(self.driver)
        self.driver.implicitly_wait(10)
        inv.findByID(values.welskip).click()
        sleep(3)
        inv.findByID(values.welcabtn).click()
        name = inv.findByXpath(invalid.invaltoast).text
        print(name)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\name_alert.jpg")

        inv.findByID(values.welname).send_keys("Test")
        inv.findByID(values.welcabtn).click()
        email = inv.findByXpath(invalid.invaltoast).text
        print(email)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\email_alert.jpg")

        inv.findByID(values.welemail).send_keys("aaaa")
        inv.findByID(values.welcabtn).click()
        invalid_email = inv.findByXpath(invalid.invaltoast).text
        print(invalid_email)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\invalid_email_alert.jpg")
        sleep(3)

        inv.findByID(values.welemail).clear()
        inv.findByID(values.welphno).send_keys("11111")
        inv.findByID(values.welcabtn).click()
        sleep(3)
        invalid_phonecode = inv.findByXpath(invalid.invaltoast).text
        print(invalid_phonecode)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\invalid_phonecode_alert.jpg")

        inv.findByID(values.welphno).clear()
        inv.findByID(values.welcode).send_keys(91)
        inv.findByID(values.welcabtn).click()
        phone = inv.findByXpath(invalid.invaltoast).text
        print(phone)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\phone_alert.jpg")

        inv.findByID(values.welphno).send_keys("90000")
        inv.findByID(values.welcabtn).click()
        sleep(3)
        inva_phno = inv.findByXpath(invalid.invaltoast).text
        print(inva_phno)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\inva_phno.jpg")

        inv.findByID(values.wellogin).click()
        inv.findByID(values.logbtn).click()
        logem = inv.findByXpath(invalid.invaltoast).text
        print(logem)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\logem.jpg")

        inv.findByID(values.logemail).send_keys("demo")
        inv.findByID(values.logbtn).click()
        logeminv = inv.findByXpath(invalid.invaltoast).text
        print(logeminv)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\logeminv.jpg")

        inv.findByID(values.logemail).clear()
        inv.findByID(values.logphno).send_keys("6666")
        inv.findByID(values.logbtn).click()
        logcode = inv.findByXpath(invalid.invaltoast).text
        print(logcode)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\logcode.jpg")

        inv.findByID(values.logcode).send_keys("91")
        inv.findByID(values.logbtn).click()
        sleep(3)
        inv.findByID(values.logalert).click()
        loginvphno = inv.findByXpath(invalid.invaltoast).text
        print(loginvphno)
        self.driver.get_screenshot_as_file("C:\\Users\\cprakash\\OneDrive - HUBBELL INC\\Documents\\cp\\Personal\\Others\\Android_Appium\\Screen_shots\\loginvphno.jpg")







    def welcome(self):
        wel =Findpat(self.driver)
        self.driver.implicitly_wait(10)
        wel.findByID(values.logcode).clear()
        wel.findByID(values.logphno).clear()
        wel.findByID(values.logemail).send_keys("demo@hubbell.com")
        wel.findByID(values.logbtn).click()
        wel.findByID(values.logalert).click()
        wel.findByID(values.logotp1).send_keys("1")
        wel.findByID(values.logotp2).send_keys("2")
        wel.findByID(values.logotp3).send_keys("3")
        wel.findByID(values.logotp4).send_keys("4")
        wel.findByID(values.logver).click()
        time.sleep(5)
        wel.findByID(values.loggpay).click()
        time.sleep(5)
        self.driver.press_keycode(4)


    def home(self):
        homescrn = Findpat(self.driver)
        homescrn.findByID(home.homnot).click()
        homescrn.findByID(home.homnotbk).click()
        homescrn.findByID(home.homhelp).click()
        homescrn.findByID(home.homfb).click()
        homescrn.findByID(home.homfbsub).send_keys("Test")
        homescrn.findByID(home.homfbcomm).send_keys("Test entered")
        homescrn.findByID(home.homfbsubm).click()
        homescrn.findByID(home.homfbthnk).click()
        homescrn.findByID(home.homfbbk).click()
        homescrn.findByID(home.homnavacct).click()
        homescrn.findByID(home.hompractrn).click()
        homescrn.findByID(home.homprtrnbk).click()
        homescrn.findByID(home.homprteco).click()
        homescrn.findByID(home.homprtecobk).click()
        homescrn.findByID(home.hompr).click()
        homescrn.findByID(home.homprna).clear()
        homescrn.findByID(home.homprna).send_keys("Demo Hubbell")
        self.driver.press_keycode(66)
        homescrn.findByID(home.homlogout).click()
        homescrn.findByID(home.homlogoutalrt).click()


















    '''def teardown(self):
        self.driver.quit'''


