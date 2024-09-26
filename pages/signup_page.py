import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *
import locators


class SignUpPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def select_plan(self, cycle):
        cycle_radiobutton = getattr(locators, f"{cycle}_RADIO_BUTTON")
        self.click(cycle_radiobutton)
        print(f'>>> Selected {cycle} plan')

    def register_in_signup_page(self):
        print(f'>>> Registering in Signup page...')
        self.enter_text(SIGNUP_NAME_FIELD, common_variables.supplement_funnel_name)
        self.enter_text(SIGNUP_EMAIL_FIELD, common_variables.supplement_funnel_email)
        self.enter_text(SIGNUP_PASSWORD_FIELD, RD.password(8))
        self.populate_cc_details(submit_button=SIGNUP_ACTIVATE_MEMBERSHIP_BUTTON)
        self.wait_for_navigation(getattr(common_variables, f'{common_variables.series}_booster_upsale_url'), timeout=20000)
        print(f'>>> Successfully registered in Signup page')