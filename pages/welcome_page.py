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

    def skip_survey(self):
        self.context.page.locator(SKIP_SURVEY_BUTTON).click()
        self.wait_for_navigation(common_variables.survery_page_url, timeout=30000)
        print('===> Skipped survery')
        self.context.page.locator(SKIP_HEALTH_TRACK_BUTTON).click()
        print('===> Skipped health track')
        self.wait_for_navigation(common_variables.client_welcome_page_url, timeout=30000)
        self.context.page.locator(GO_TO_ZONIA_BUTTON).click()
        print('===> Navigated to user home page')
