import common_variables
from common_functions import random_data as RD
from features.lib.pages.base_page_object import BasePage


class SignUpPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def sign_up(self, bill_cycle, name, email, password):
        if bill_cycle not in ['monthly', 'quarterly', 'annually']:
            raise Exception(f'Bill cycle "{bill_cycle}" is not valid!')
        self.click(f'{bill_cycle}_radio_button')
        self.enter_text(name, 'signup_name_field')
        self.enter_text(email, 'signup_email_field')
        self.enter_text(password, 'signup_password_field')
        self.populate_cc_details()
        self.click('signup_activate_button')
        self.wait_for_url_change(common_variables.booster_upsale_url)

    def sign_up_with_random_data(self, bill_cycle):
        if bill_cycle not in ['monthly', 'quarterly', 'annually']:
            raise Exception(f'Bill cycle "{bill_cycle}" is not valid!')
        self.click(f'{bill_cycle}_radio_button')
        self.enter_text(RD.full_name(), 'signup_name_field')
        self.enter_text(RD.email(), 'signup_email_field')
        self.enter_text(RD.password(), 'signup_password_field')
        self.populate_cc_details()
        self.click('signup_activate_button')
        self.wait_for_partial_url_change(common_variables.sign_up_url, common_variables.booster_upsale_url)

    def populate_cc_details(self):
        self.switch_to_iframe('signup_cc_number_iframe')
        self.enter_text(common_variables.test_cc_number, 'signup_cc_number_field')
        self.switch_to_default_content()
        self.switch_to_iframe('signup_cc_expiration_iframe')
        self.enter_text(common_variables.test_cc_expiration_date, 'signup_cc_expiration_field')
        self.switch_to_default_content()
        self.switch_to_iframe('signup_cc_cvv_iframe')
        self.enter_text(common_variables.test_cc_cvv, 'signup_cc_cvv_field')
        self.switch_to_default_content()
        self.switch_to_iframe('signup_cc_zip_iframe')
        self.enter_text(common_variables.test_cc_zip, 'signup_cc_zip_field')
        self.switch_to_default_content()
