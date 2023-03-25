import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
#First Specify the locators in a page
    REFERENCES = (By.XPATH,"//a[@title='References']")
    PHPCompilerButton = (By.XPATH,"//a[contains(@href,'php_compiler.asp')]")
    def __init__(self,driver):
        super().__init__(driver)


    def click_on(self,locator):
        self.click_element(locator)

    def hover_on(self,locator):
        self.hover_on_element(locator)