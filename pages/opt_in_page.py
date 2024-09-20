import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *


class OptInPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def register_in_opt_in_page(self):
        common_variables.supplement_funnel_email = RD.automation_template_email()
        common_variables.supplement_funnel_name = RD.automation_first_name()
        print(f'===> Registering in Main Opt in page...')
        # self.click(__dict__[button_locator])
        # time.sleep(2)
        self.enter_text(OPTIN_NAME_FIELD, common_variables.supplement_funnel_name)
        self.enter_text(OPTIN_EMAIL_FIELD, common_variables.supplement_funnel_email)
        # self.click(PHONE_CHECKBOX)
        # self.enter_text(PHONE_FIELD, RD.phone_number())
        self.click(REGISTER_BUTTON)
        self.wait_for_navigation(getattr(common_variables, f'{common_variables.series}_join_zonia_url'), timeout=20000)
        self.verify_element_visible(JOIN_ZONIA_ID_BUTTON)
        print(f'===> Successful')