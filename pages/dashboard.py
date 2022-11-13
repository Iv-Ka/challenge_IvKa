from pages.base_page import BasePage


class Dashboard(BasePage):
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















