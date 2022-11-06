from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"

    main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"

    players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"

    Language_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"

    sign_out_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"





