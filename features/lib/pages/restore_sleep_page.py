import time
import common_variables
import common_functions.random_data as RD
from features.lib.pages.base_page_object import BasePage


class RestoreSleepPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def buy_bottles(self, amount):
        self.scroll_to_element(f'add_{amount}_button')
        self.click(f'add_{amount}_button')
        self.enter_text(RD.first_name(), 'rs_first_name_field')
        self.enter_text(RD.last_name(), 'rs_last_name_field')
        self.enter_text(RD.email(), 'rs_email_field')
        self.enter_text(RD.phone_number(), 'rs_phone_field')
        self.enter_text(RD.address_line(), 'rs_address_field')
        self.enter_text(RD.town(), 'rs_city_field')
        self.enter_text('USA', 'rs_country_field')
        self.enter_text('NY', 'rs_state_field')
        self.enter_text(RD.postcode(), 'rs_zip_field')
        self.populate_cc_details()
        self.click('rs_place_order_button')
        self.wait_for_partial_url_change(common_variables.restore_sleep_first_upsell_url)