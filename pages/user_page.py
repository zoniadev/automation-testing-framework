import time
from pages.base_page_object import BasePage
from locators import *


class UserPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def verify_registration(self):
        name = self.context.test_data['name']
        email = self.context.test_data['email']
        password = self.context.test_data['password']
        
        name_on_page = self.context.page.locator(USER_MENU_BUTTON).inner_text()
        assert name in name_on_page, (f'Expected name to be '
                                                                         f'"{name}",'
                                                                         f' but it is "{name_on_page}"!')
        print('===> Verified registration')
        print(f'Email: {email}')
        print(f'Pass: {password}')
