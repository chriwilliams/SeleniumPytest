import pytest
import os
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

#imports for  dotenv to place credentials in a secret folder
# for reference https://www.youtube.com/watch?v=YdgIWTYQ69A
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")



#First thing is to use the init_driver fixture located in Basetest which focuses on the webdriver setup and browser
class TestLogin(BaseTest):

    def test_signup_link_visible(self):
        # this is the instance of the LoginPage class, in which I can get all the related methods. I chose to name it loginPage.
        # adding a constructor to the LoginPage class alows me to do this.
        self.loginPage = LoginPage(self.driver)
        # I am using the is_signup_link_exist method from the LoginPage class for this test and storing the return statement in a variable named flag
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.get_title(TestData.LOGINN_PAGE_TITLE)
        assert title == TestData.LOGINN_PAGE_TITLE

    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        #self.LoginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        #credentials are now in a .env folder
        self.LoginPage.do_login(USERNAME, PASSWORD)



