import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *
import locators


class SignUpPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def select_plan(self, cycle):
        cycle_radiobutton = getattr(locators, f"{cycle}_RADIO_BUTTON")
        self.context.page.locator(cycle_radiobutton).click()
        print(f'>>> Selected {cycle} plan')

    def register_in_signup_page(self, cycle):
        print(f'>>> Registering in Signup page...')
        self.context.page.locator(SIGNUP_NAME_FIELD).fill(common_variables.supplement_funnel_name)
        self.context.page.locator(SIGNUP_EMAIL_FIELD).fill(common_variables.supplement_funnel_email)
        common_variables.supplement_funnel_password = RD.password(8)
        self.context.page.locator(SIGNUP_PASSWORD_FIELD).fill(common_variables.supplement_funnel_password)
        print(f'===> User email is: {common_variables.supplement_funnel_email}')
        self.populate_cc_details(submit_button=SIGNUP_ACTIVATE_MEMBERSHIP_BUTTON)
        if common_variables.funnel_prefix not in ['km', 'twl', 'ad', 'cr']:
            if cycle == 'lifetime':
                cycle = 'monthly'
        if common_variables.is_replay_weekend:
            if cycle in ['lifetime', 'annually']:
                common_variables.docuseries_address_will_appear = True
                print('Address popup should appear next page')
            self.wait_for_navigation(
                getattr(common_variables, f'{common_variables.funnel_prefix}_masterclass_url'),
                timeout=30000)
        elif common_variables.funnel_prefix == 'pc':
            self.wait_for_navigation(
                getattr(common_variables, f'{common_variables.funnel_prefix}_restore_sleep_url'),
                timeout=30000)
        else:
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel_prefix}_booster_{cycle}_upsale_url'), timeout=30000)
        print(f'>>> Successfully registered in Signup page')