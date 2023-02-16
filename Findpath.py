from selenium.webdriver.common.by import By


class Findpat:

    def __init__(self, driver):
        self.driver = driver

    def findByXpath(self, pathtofind):
        return self.driver.find_element(By.XPATH, pathtofind)

    def findByXPATH(self, pathtofind):
        return self.driver.find_elements(By.XPATH, pathtofind)

    def findByID(self, pathtofind):
        return self.driver.find_element(By.ID, pathtofind)

    def findByCSS(self, pathtofind):
        return self.driver.find_element(By.CSS_SELECTOR, pathtofind)

    def findByLink(self, pathtofind):
        return self.driver.find_element(By.LINK_TEXT, pathtofind)