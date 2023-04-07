from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class TestData:
    CHROME_DRIVER = webdriver.Chrome(ChromeDriverManager().install())
    firefox_binary = FirefoxBinary()
    #FIREFOX_DRIVER = webdriver.Firefox(firefox_binary=firefox_binary)
    FIREFOX_DRIVER = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    BASE_URL = "https://app.hubspot.com/login"
    # USERNAME = "chwill782gmail.com"
    # PASSWORD = "Willie4pres2"

    LOGINN_PAGE_TITLE = "HubSpot Login"
