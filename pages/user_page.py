import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage


class UserPageLocators:
    SKIP_QUESTIONS_BUTTON = "//*[@class='skipAndRegister']"
    USER_MENU_BUTTON = "//*[@id='subname']"


class UserPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def skip_questions(self):
        self.click(UserPageLocators.SKIP_QUESTIONS_BUTTON)
        time.sleep(3)

    def verify_registration(self):
        name_on_page = self.get_text(UserPageLocators.USER_MENU_BUTTON)
        assert common_variables.supplement_funnel_name in name_on_page, (f'Expected name to be '
                                                                         f'"{common_variables.supplement_funnel_name}",'
                                                                         f' but it is "{name_on_page}"!')
        print(f'Email: {common_variables.supplement_funnel_email}')
        print(f'Pass: {common_variables.supplement_funnel_password}')


