import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *
import locators


class SupplementStartPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def supplement_funnel_buy_bottles(self, amount, funnel):
        self.disable_chat()
        self.handle_cookie_banner()
        from playwright.sync_api import expect
        self.context.supplement_funnel_email = RD.automation_template_email()
        self.context.supplement_funnel_name = RD.automation_first_name()
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
        self.enter_text(FIRST_NAME_FIELD, self.context.supplement_funnel_name, method="safe_fill")
        self.enter_text(LAST_NAME_FIELD, RD.last_name())
        self.enter_text(EMAIL_FIELD, self.context.supplement_funnel_email)
        self.enter_text(PHONE_FIELD, RD.phone_number())
        self.enter_text(ADDRESS_FIELD, RD.address_line())
        self.enter_text(CITY_FIELD, RD.town())
        print(f'Funnel: {self.context.funnel}')
        if self.context.funnel in ['restore_vision', 'restore_vision_b2g3']:
            self.context.page.locator(COUNTRY_FIELD).select_option('USA')
        else:
            self.enter_text(COUNTRY_FIELD, 'USA')
        self.enter_text(STATE_FIELD, 'CA')
        self.enter_text(ZIP_FIELD, RD.postcode())
        print(f'===> User email is: {self.context.supplement_funnel_email}')
        self.populate_cc_details()
        self.wait_for_navigation(
            getattr(common_variables, f"{funnel.lower().replace(' ', '_')}_first_upsell_url"), timeout=30000)
        expect(self.context.page.locator(YES_UPGRADE_BUTTON)).to_be_visible()
        print(f'===> Successfully bought {amount} bottle')
