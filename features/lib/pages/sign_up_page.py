import common_variables
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

