import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *


class WelcomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def create_password(self):
        common_variables.supplement_funnel_password = RD.password()
        time.sleep(0.5)
        self.find_element(PASSWORD_POPUP_FIELD).press_sequentially(common_variables.supplement_funnel_password)
        time.sleep(0.5)
        self.click(SAVE_PASSWORD_BUTTON)

    def skip_linking_social_media_accounts(self):
        self.click(SKIP_LINKING_BUTTON)
        time.sleep(1)


