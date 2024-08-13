import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage


class WelcomePageLocators:
    PASSWORD_POPUP_FIELD = "//*[@placeholder='Enter password']"
    SAVE_PASSWORD_BUTTON = "//*[@class[contains(., 'save-password')] and @type='submit']"
    SKIP_LINKING_BUTTON = "//button[@class='skip-login']"


class WelcomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def create_password(self):
        common_variables.supplement_funnel_password = RD.password()
        time.sleep(0.5)
        self.find_element(WelcomePageLocators.PASSWORD_POPUP_FIELD).press_sequentially(common_variables.supplement_funnel_password)
        time.sleep(0.5)
        self.click(WelcomePageLocators.SAVE_PASSWORD_BUTTON)

    def skip_linking_social_media_accounts(self):
        self.click(WelcomePageLocators.SKIP_LINKING_BUTTON)
        time.sleep(1)


