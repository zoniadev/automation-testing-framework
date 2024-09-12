import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *


class SupplementStartPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def buy_bottles(self, amount):
        common_variables.supplement_funnel_email = RD.automation_template_email()
        common_variables.supplement_funnel_name = RD.automation_first_name()
        button_locator = f"ORDER_{amount}_BOTTLES_BUTTON"
        print(f'===> Buying {amount} bottle...')
        self.click(__dict__[button_locator])
        time.sleep(2)
        self.find_element(FIRST_NAME_FIELD).press_sequentially(common_variables.supplement_funnel_name)
        self.find_element(LAST_NAME_FIELD).press_sequentially(RD.last_name())
        self.find_element(EMAIL_FIELD).press_sequentially(common_variables.supplement_funnel_email)
        self.find_element(PHONE_FIELD).press_sequentially(RD.phone_number())
        self.find_element(ADDRESS_FIELD).press_sequentially(RD.address_line())
        self.find_element(CITY_FIELD).press_sequentially(RD.town())
        self.find_element(COUNTRY_FIELD).press_sequentially('USA')
        self.find_element(STATE_FIELD).press_sequentially('CA')
        self.find_element(ZIP_FIELD).press_sequentially(RD.postcode())
        self.populate_cc_details()
        self.wait_for_navigation(common_variables.restore_sleep_first_upsell_url, timeout=20000)
        self.verify_element_visible(YES_UPGRADE_BUTTON)
        print(f'===> Successfully bought {amount} bottle')