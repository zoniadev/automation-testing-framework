import time

import common_variables
from features.lib.pages.base_page_object import BasePage


class OptInPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def verify_register_buttons_navigation(self):
        button_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.verify_element_visible('form_logo')
        self.verify_element_in_viewport('form_logo')
        for item in button_numbers:
            self.scroll_to_element(f'register{str(item)}_button')
            try:
                self.verify_element_visible('close_popup_button', 5)
                self.click('close_popup_button')
            except:
                pass
            time.sleep(1)
            self.click(f'register{str(item)}_button')
            self.verify_element_visible('form_logo')
            time.sleep(1)
            self.verify_element_in_viewport('form_logo')

    def register(self, name, email):
        self.verify_element_visible('close_popup_button')
        self.click('close_popup_button')
        self.enter_text(name, 'first_name_field')
        self.enter_text(email, 'email_field')
        self.click('register_button')
        self.wait_for_url_change(common_variables.join_zonia_url)