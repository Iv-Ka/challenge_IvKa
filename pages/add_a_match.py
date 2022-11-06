from pages.base_page import BasePage


class add_a_match(BasePage)

    submit_button_xpath = "//*[@type='submit']"

    clear_button_xpath = "// span[contains(text( ),'Clear')]"

    My_team_xpath = "//*[@name='myTeam']"

    Enemy_team_xpath = "//*[@name='enemyTeam']"

    My_team_score_xpath = "//*[@name='myTeamScore']"