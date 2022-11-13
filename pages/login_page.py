from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "// button[contains(@type,'submit')]"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, param):

    user_login.type_in_password('Test-1234')
        pass


    def click_on_the_sign_in_button(self):

    user_login.click_on_the_sign_in_button()
        pass
