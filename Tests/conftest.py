import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = TestData.CHROME_DRIVER
    if request.param == 'firefox':
        web_driver = TestData.FIREFOX_DRIVER
    request.cls.driver = web_driver
    yield
    web_driver.close()


