import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

#Base Page will include the actual webdriver functions like click ,hover etc
#Base Page's driver will be instantiated via other page objects created in test methods
class BasePage:

    def __init__(self,driver):
        self.driver=driver
        self.action=ActionChains(self.driver)

    @allure.step('clicking on element located by "{0}"')
    def click_element(self,locator):
        elementOne=WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))
        elementOne.click()

    @allure.step('hover on element located by "{0}"')
    def hover_on_element(self,locator):
        elementOne=WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))
        self.action.move_to_element(elementOne).perform()