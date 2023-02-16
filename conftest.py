import os
import pytest

from appium import webdriver

@pytest.fixture()
def setup(request):
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': 'D:\\app-release.apk',
                'platformName': 'Android',
                'platformVersion': '8',
                'deviceName': 'Samsung Galaxy S7 Edge',
                'appium: appPackage': 'com.hubbell.chargecenter',
                'appium:appActivity': 'com.hubbell.chargecenter.tutorials.initial.InitialTutorialActivity'

            })
        request.cls.driver = driver
