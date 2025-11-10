import time
import random
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
        time.sleep(1)
        self.context.page.locator(SKIP_SURVEY_BUTTON).click()
        self.wait_for_navigation(common_variables.survey_page_url, timeout=30000)
        print('===> Skipped survery')
        time.sleep(1)
        random_heath_track_selection = ['stress-management-sleep-lbl', 'energy-reboot-lbl', 'autoimmunity-immune-rejuventaion-lbl',
                                        'brain-power-boost-lbl', 'metabolic-health-weight-managment-lbl', 'cancer-support-lbl',
                                        'skip-health-track-btn']
        random_selection = random.choice(random_heath_track_selection)
        element_to_select = f'//*[@id="{random_selection}"]'
        print(f'===> Selecting {random_selection} in Health Track')
        self.context.page.locator(element_to_select).click()
        print('===> Skipped health track')
        self.wait_for_navigation(common_variables.client_welcome_page_url, timeout=30000)
        self.context.page.locator(GO_TO_ZONIA_BUTTON).click()
        print('===> Navigated to user home page')
