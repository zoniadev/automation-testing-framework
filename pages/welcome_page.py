import time
import random
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *
from playwright.sync_api import expect


class WelcomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def create_password(self):
        self.context.supplement_funnel_password = RD.password()
        self.context.page.locator(PASSWORD_POPUP_FIELD).click(timeout=20000)
        time.sleep(0.5)
        self.context.page.locator(PASSWORD_POPUP_FIELD).press_sequentially(self.context.supplement_funnel_password)
        time.sleep(0.5)
        self.context.page.locator(SAVE_PASSWORD_BUTTON).click()

    def skip_survey(self):
        time.sleep(1) # Keep a small sleep just in case, but rely more on explicit wait
        self.handle_cookie_banner()
        if self.context.docuseries_prefix != 'fs':
            # Explicitly wait for the SKIP_SURVEY_BUTTON to be visible before clicking
            expect(self.context.page.locator(SKIP_SURVEY_BUTTON)).to_be_visible(timeout=10000)
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
            # Health track labels are populated after the navigation completes
            # (client-side fetch), so wait for the specific label to be
            # visible before clicking, instead of relying on click()'s own
            # default 30s actionability wait. Deliberately not using
            # wait_for_load_state("networkidle") here: this app has
            # continuous background network activity on this page (embedded
            # video telemetry, chat-widget polling, ad beacons), so the page
            # may never go network-idle even once fully rendered - that wait
            # was itself causing false-failure timeouts unrelated to whether
            # the label was actually ready.
            expect(self.context.page.locator(element_to_select)).to_be_visible(timeout=30000)
            self.context.page.locator(element_to_select).click()
            print('===> Skipped health track')
            self.wait_for_navigation(common_variables.client_welcome_page_url, timeout=30000)
            self.handle_cookie_banner()
            self.context.page.locator(GO_TO_ZONIA_BUTTON).click()
        else:
            self.context.page.locator(FS_GO_TO_ZONIA_BUTTON).click()
        print('===> Navigated to user home page')