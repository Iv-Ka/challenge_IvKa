import time

from pages.base_page import BasePage


class AddPlayerPage(BasePage):

    expected_title = "Add player"

    adding_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    adding_button_xpath = "//*[@id='__next']/div[1]/main//button/span"

    email_xpath = "//*[@id='__next']/div//input"

    name_xpath = "//*[@name='name']"

    surname_xpath = "//*[@name='surname']"

    submit_xpath = "//*[@type='submit']"

    age_xpath = "//*[@name='age']"

    position_xpath = "//*[@name='mainPosition']"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.adding_url) == self.expected_title

    def click_on_the_adding_player_button(self):
        self.click_on_the_element(self.adding_button_xpath)

    def type_in_email(self, email):
        self.field_send_keys(self.email_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_position(self, position):
        self.field_send_keys(self.position_xpath, position)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_xpath)
        pass
