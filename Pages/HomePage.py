from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = By.CSS_SELECTOR, "h1.dash"