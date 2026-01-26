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

    def register_in_signup_page(self, cycle, paypal=False):
        print(f'>>> Registering in Signup page...')
        self.context.page.locator(SIGNUP_NAME_FIELD).fill(common_variables.supplement_funnel_name)
        self.context.page.locator(SIGNUP_EMAIL_FIELD).fill(common_variables.supplement_funnel_email)
        common_variables.supplement_funnel_password = RD.password(8)
        self.context.page.locator(SIGNUP_PASSWORD_FIELD).fill(common_variables.supplement_funnel_password)
        print(f'===> User email is: {common_variables.supplement_funnel_email}')
        if paypal:
            self.disable_chat()
            self.pay_with_paypal()
        else:
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
        elif common_variables.bonus_episode:
            self.wait_for_navigation(
                getattr(common_variables, f'{common_variables.funnel_prefix}_masterclass_url'),
                timeout=30000)
        else:
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel_prefix}_booster_{cycle}_upsale_url'), timeout=30000)
        print(f'>>> Successfully registered in Signup page')

    def pay_with_paypal(self):
        new_page = self.switch_to_new_tab(lambda: self.context.page.locator(PAYPAL_BUTTON).click())
        # Perform login on the new page
        new_page.locator(PAYPAL_EMAIL_FIELD).fill(common_variables.paypal_email)
        new_page.locator(PAYPAL_NEXT_BUTTON).click()
        new_page.locator(PAYPAL_PASSWORD_FIELD).fill(common_variables.paypal_password)
        new_page.locator(PAYPAL_LOGIN_BUTTON).click()

        # Wait for the new page to close or navigate back to the original page
        # Assuming the new page closes after login or redirects back
        # You might need to adjust this based on the actual behavior
        # For example, if the window closes automatically:
        # new_page.wait_for_event("close")

        # If the focus needs to return to the original page
        self.context.page.bring_to_front()
