import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def get_browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="function")
def setup(request,get_browser):
    if(get_browser=="chrome"):
     p=ChromeDriverManager()
     driver = webdriver.Chrome(p.install())
    driver.get("https://www.w3schools.com/php/php_examples.asp")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()