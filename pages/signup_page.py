import time
import common_functions.random_data as RD
from common_functions.url_manager import URLManager
from pages.base_page_object import BasePage


class SignUpPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        
        # --- Locators (Defined in __init__ as per Playwright Best Practices) ---
        
        # Plan Radio Buttons
        # Using CSS selectors for cleaner syntax (works same as XPath for attributes)
        self.monthly_radio = self.page.locator("input[unique-id='monthly_new-1']")
        self.quarterly_radio = self.page.locator("input[unique-id='quarterly-1']")
        self.annually_radio = self.page.locator("input[unique-id='yearly_new-1']")
        self.lifetime_radio = self.page.locator("input[unique-id='lifetime-1']")
        
        # Form Fields
        self.name_input = self.page.locator("input[id='form-name']")
        self.email_input = self.page.locator("input[id='form-email']")
        self.password_input = self.page.locator("input[id='form-password']")
        
        # Buttons
        self.activate_membership_button = self.page.locator("button[unique-id='activate-membership-1']")

    def select_plan(self, cycle):
        """
        Selects the plan based on the cycle name.
        """
        # Map string keys to Locator objects
        # This replaces the fragile `getattr(self, f"{cycle}_RADIO_BUTTON")` logic
        plan_map = {
            'MONTHLY': self.monthly_radio,
            'QUARTERLY': self.quarterly_radio,
            'ANNUALLY': self.annually_radio,
            'LIFETIME': self.lifetime_radio
        }
        
        if cycle not in plan_map:
            raise ValueError(f"Unknown plan cycle: {cycle}")
            
        plan_map[cycle].click()
        print(f'>>> Selected {cycle} plan')

    def register_in_signup_page(self, cycle):
        print(f'>>> Registering in Signup page...')
        
        # Get data from context
        name = self.context.test_data['name']
        email = self.context.test_data['email']
        
        self.name_input.fill(name)
        self.email_input.fill(email)
        
        password = RD.password(8)
        self.context.test_data['password'] = password
        
        self.password_input.fill(password)
        print(f'===> User email is: {email}')
        
        # Pass the Locator object directly
        self.populate_cc_details(submit_button=self.activate_membership_button)
        
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