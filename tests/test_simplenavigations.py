import json

import allure
import pytest
from allure_commons.types import AttachmentType

from pages.HomePage import HomePage
from tests import BaseTest


@pytest.mark.usefixtures("setup")
class TestHomePage(BaseTest.BaseTest):
# Taking Screenshots
    @pytest.mark.sanity
    def test_one(self):
        self.homePage=HomePage(self.driver)
        self.homePage.click_on(HomePage.PHPCompilerButton)
        allure.attach(self.driver.get_screenshot_as_png(),name="testOne",attachment_type=AttachmentType.PNG)


    @pytest.mark.sanity
    def test_two(self):
        self.homePage=HomePage(self.driver)
        self.homePage.hover_on_element(HomePage.REFERENCES)
        allure.attach(self.driver.get_screenshot_as_png(), name="testTwo", attachment_type=AttachmentType.PNG)



