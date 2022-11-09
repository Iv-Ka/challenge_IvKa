from pages.base_page import BasePage


class add_a_match(BasePage)

    submit_button_xpath = "//*[@type='submit']"

    clear_button_xpath = "// span[contains(text( ),'Clear')]"

    My_team_xpath = "//*[@name='myTeam']"

    Enemy_team_xpath = "//*[@name='enemyTeam']"

    My_team_score_xpath = "//*[@name='myTeamScore']"

    date_xpath = "//*[@type='date']"

    At_home_xpath = "// span[contains(text( ),'Match at home')]"

    Out_home_xpath = "// span[contains(text( ),'Match out home')]"

    T_shirt_xpath = "//*[@name='tshirt']"

    league_xpath = "//*[@name='league']"

    time_played_xpath = "//*[@name='timePlayed']"

    number_xpath = "//*[@name='number']"

    web_match_xpath = "//*[@name='webMatch']"

    general_xpath = "//*[@name='general']"

    rating_xpath = "//*[@name='rating']"

pass



