import time
import common_functions.random_data as RD
from common_functions.url_manager import URLManager
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
        
        # Get data from context
        name = self.context.test_data['name']
        email = self.context.test_data['email']
        
        self.context.page.locator(SIGNUP_NAME_FIELD).fill(name)
        self.context.page.locator(SIGNUP_EMAIL_FIELD).fill(email)
        
        password = RD.password(8)
        self.context.test_data['password'] = password
        
        self.context.page.locator(SIGNUP_PASSWORD_FIELD).fill(password)
        print(f'===> User email is: {email}')
        
        self.populate_cc_details(submit_button=SIGNUP_ACTIVATE_MEMBERSHIP_BUTTON)
        
        funnel_prefix = self.context.test_data['funnel_prefix']
        is_replay_weekend = self.context.test_data['is_replay_weekend']
        bonus_episode = self.context.test_data['bonus_episode']
        
        if funnel_prefix not in ['km', 'twl', 'ad', 'cr']:
            if cycle == 'lifetime':
                cycle = 'monthly'
                
        if is_replay_weekend:
            if cycle in ['lifetime', 'annually']:
                self.context.test_data['address_will_appear'] = True
                print('Address popup should appear next page')
            self.wait_for_navigation(
                URLManager.get_url(f'{funnel_prefix}_masterclass_url'),
                timeout=30000)
        elif funnel_prefix == 'pc':
            self.wait_for_navigation(
                URLManager.get_url(f'{funnel_prefix}_restore_sleep_url'),
                timeout=30000)
        elif bonus_episode:
            self.wait_for_navigation(
                URLManager.get_url(f'{funnel_prefix}_masterclass_url'),
                timeout=30000)
        else:
            self.wait_for_navigation(URLManager.get_url(f'{funnel_prefix}_booster_{cycle}_upsale_url'), timeout=30000)
        print(f'>>> Successfully registered in Signup page')