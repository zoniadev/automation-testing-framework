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
        self.context.page.locator(PASSWORD_POPUP_FIELD).click(timeout=20000)
        self.context.page.locator(PASSWORD_POPUP_FIELD).press_sequentially(common_variables.supplement_funnel_password)
        self.context.page.locator(SAVE_PASSWORD_BUTTON).click()

    def skip_linking_social_media_accounts(self):
        time.sleep(0.5)
        self.context.page.locator(SKIP_LINKING_BUTTON).click()
