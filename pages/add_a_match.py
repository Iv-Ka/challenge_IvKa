from pages.base_page import BasePage


class add_a_match(BasePage)

    submit_button_xpath = "//*[@type='submit']"

    clear_button_xpath = "// span[contains(text( ),'Clear')]"

    my_team_xpath = "//*[@name='myTeam']"

    enemy_team_xpath = "//*[@name='enemyTeam']"

    my_team_score_xpath = "//*[@name='myTeamScore']"

    date_xpath = "//*[@type='date']"

    at_home_xpath = "// span[contains(text( ),'Match at home')]"

    out_home_xpath = "// span[contains(text( ),'Match out home')]"

    t_shirt_xpath = "//*[@name='tshirt']"

    league_xpath = "//*[@name='league']"

    time_played_xpath = "//*[@name='timePlayed']"

    number_xpath = "//*[@name='number']"

    web_match_xpath = "//*[@name='webMatch']"

    general_xpath = "//*[@name='general']"

    rating_xpath = "//*[@name='rating']"

pass



