import time
from pages.base_page_object import BasePage


class UserPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        
        # --- Locators ---
        self.skip_questions_button = self.page.locator("//*[@class='skipAndRegister']")
        self.user_menu_button = self.page.locator("//li[@id='top_header_menu_account']//a[@id='subname']")

    def verify_registration(self):
        name = self.context.test_data['name']
        email = self.context.test_data['email']
        password = self.context.test_data['password']
        
        name_on_page = self.user_menu_button.inner_text()
        assert name in name_on_page, (f'Expected name to be '
                                                                         f'"{name}",'
                                                                         f' but it is "{name_on_page}"!')
        print('===> Verified registration')
        print(f'Email: {email}')
        print(f'Pass: {password}')
