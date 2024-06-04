import common_variables
from features.lib.pages.base_page_object import BasePage


class OptInPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def register(self, name, email):
        self.verify_element_visible('close_popup_button')
        self.click('close_popup_button')
        self.enter_text(name, 'first_name_field')
        self.enter_text(email, 'email_field')
        self.click('register_button')
        self.wait_for_url_change(common_variables.join_zonia_url)
        # self.verify_url(common_variables.join_zonia_url)