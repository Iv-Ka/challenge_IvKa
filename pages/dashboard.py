import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"

    dashboard_url = "https://scouts-test.futbolkolektyw.pl"

    adding_button_xpath = "//*[@id='__next']/div[1]/main//button/span"

    email_xpath = "//*[@id='__next']/div//input"

    name_xpath = "//*[@name='name']"

    surname_xpath = "//*[@name='surname']"

    submit_xpath = "//*[@type='submit']"

    age_xpath = "//*[@name='age']"

    position_xpath = "//*[@name='mainPosition']"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

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
        self.field_send_keys(self.position_xpath)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_xpath)
        pass

    button_xpath = "//*[@id='login']"

    main_page_xpath = "// span[contains(text( ),'Main page')]"

    players_xpath = "// span[contains(text( ),'Players')]"

    language_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"

    sign_out_xpath = "// span[contains(text( ),'Sign out')]"

    reports_count_xpath = "// div[contains(text( ),'Reports count')]"

    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    add_player_xpath2 = "// span[contains(text( ),'Add player')]"

    download_button = "// button[contains(@title,'Download CSV')]"

    print_button_xpath = "// button[contains(@title,'Print')]"

    filter_table_xpath = "// button[contains(@title,'Filter Table')]"

    view_columns_xpath = "// button[contains(@title,'View Columns')]"

    arrow_next_xpath = "//*[@data-testid='pagination-next']"

    arrow_previous_xpath = "//*[@data-testid='pagination-back']"

    add_link_to_Youtube_xpath = "//*[@aria-label='Add link to Youtube']"


pass
