import time
import common_functions.random_data as RD
from common_functions.url_manager import URLManager
from pages.base_page_object import BasePage
from locators import *
import locators


class SupplementStartPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def supplement_funnel_buy_bottles(self, amount, funnel):
        self.disable_chat()
        from playwright.sync_api import expect
        
        # Generate and store user data in context
        self.context.test_data['email'] = RD.automation_template_email()
        self.context.test_data['name'] = RD.automation_first_name()
        
        print(f'===> Buying {amount} bottle...')
        if amount == '11':
            self.context.page.locator(BUY_5_BOTTLES_BUTTON).click()
            self.context.page.locator(BUY_SPECIAL_B4G7_OFFER_BUTTON).click()
        elif amount == '5':
            self.context.page.locator(BUY_5_BOTTLES_BUTTON).click()
            self.context.page.locator(BUY_MOST_POPULAR_BUTTON).click()
        else:
            button_locator = getattr(locators, f"BUY_{amount}_BOTTLES_BUTTON")
            self.context.page.locator(button_locator).click()
            
        self.safe_fill(FIRST_NAME_FIELD, self.context.test_data['name'])
        self.context.page.locator(LAST_NAME_FIELD).fill(RD.last_name())
        self.context.page.locator(EMAIL_FIELD).fill(self.context.test_data['email'])
        self.context.page.locator(PHONE_FIELD).fill(RD.phone_number())
        self.context.page.locator(ADDRESS_FIELD).fill(RD.address_line())
        self.context.page.locator(CITY_FIELD).fill(RD.town())
        
        current_funnel = self.context.test_data['funnel']
        print(f'Funnel: {current_funnel}')
        
        if current_funnel in ['restore_vision', 'restore_vision_b2g3']:
            self.context.page.locator(COUNTRY_FIELD).select_option('USA')
        else:
            self.context.page.locator(COUNTRY_FIELD).fill('USA')
            
        self.context.page.locator(STATE_FIELD).fill('CA')
        self.context.page.locator(ZIP_FIELD).fill(RD.postcode())
        print(f'===> User email is: {self.context.test_data["email"]}')
        
        self.populate_cc_details()
        
        next_url_key = f"{funnel.lower().replace(' ', '_')}_first_upsell_url"
        self.wait_for_navigation(URLManager.get_url(next_url_key), timeout=30000)

        expect(self.context.page.locator(YES_UPGRADE_BUTTON)).to_be_visible()
        print(f'===> Successfully bought {amount} bottle')
