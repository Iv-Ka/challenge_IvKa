import os
import time
import unittest
from selenium import webdriver

from pages.add_player import AddPlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddingPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_adding_player_button()
        add_player = AddPlayerPage(self.driver)
        add_player.type_in_email('user06@getnada.com')
        add_player.type_in_name('Zlatan')
        add_player.type_in_surname('Ib-ra')
        add_player.type_in_age('12121999')
        add_player.type_in_position('1')
        add_player.click_on_submit_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
        self.driver.quit()
