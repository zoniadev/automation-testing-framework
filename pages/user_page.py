import time
import common_variables
from pages.base_page_object import BasePage
from locators import *


class UserPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def verify_registration(self):
        name_on_page = self.context.page.locator(USER_MENU_BUTTON).inner_text()
        assert common_variables.supplement_funnel_name in name_on_page, (f'Expected name to be '
                                                                         f'"{common_variables.supplement_funnel_name}",'
                                                                         f' but it is "{name_on_page}"!')
        print('===> Verified registration')
        print(f'Email: {common_variables.supplement_funnel_email}')
        print(f'Pass: {common_variables.supplement_funnel_password}')


