import time
import random
import common_functions.random_data as RD
from common_functions.url_manager import URLManager
from pages.base_page_object import BasePage


class WelcomePage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        
        # --- Locators ---
        self.password_popup_field = self.page.locator("//*[@placeholder='Enter password']")
        self.save_password_button = self.page.locator("//*[@class[contains(., 'save-password')] and @type='submit']")
        self.skip_linking_button = self.page.locator("//*[@unique-id='home-btn-1']")
        self.skip_survey_button = self.page.locator("//*[@unique-identifier='skip-survey-btn-1']")
        self.go_to_zonia_button = self.page.locator("//*[@unique-identifier='go-to-zonia-btn-1']")

    def create_password(self):
        password = RD.password()
        self.context.test_data['password'] = password
        
        self.password_popup_field.click(timeout=20000)
        time.sleep(0.5)
        self.password_popup_field.press_sequentially(password)
        time.sleep(0.5)
        self.save_password_button.click()

    def skip_survey(self):
        time.sleep(1)
        self.handle_cookie_banner()
        self.skip_survey_button.click()
        self.wait_for_navigation(URLManager.get_url('survey_page_url'), timeout=30000)
        print('===> Skipped survery')
        time.sleep(1)
        random_heath_track_selection = ['stress-management-sleep-lbl', 'energy-reboot-lbl', 'autoimmunity-immune-rejuventaion-lbl',
                                        'brain-power-boost-lbl', 'metabolic-health-weight-managment-lbl', 'cancer-support-lbl',
                                        'skip-health-track-btn']
        random_selection = random.choice(random_heath_track_selection)
        element_to_select = f'//*[@id="{random_selection}"]'
        print(f'===> Selecting {random_selection} in Health Track')
        self.page.locator(element_to_select).click()
        print('===> Skipped health track')
        self.wait_for_navigation(URLManager.get_url('client_welcome_page_url'), timeout=30000)
        self.handle_cookie_banner()
        self.go_to_zonia_button.click()
        print('===> Navigated to user home page')
