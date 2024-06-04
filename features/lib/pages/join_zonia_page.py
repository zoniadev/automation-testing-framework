import common_variables
from features.lib.pages.base_page_object import BasePage


class JoinZoniaPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def join(self):
        self.click('join_button')
        self.wait_for_url_change(common_variables.sign_up_url)
