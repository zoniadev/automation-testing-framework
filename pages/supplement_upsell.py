import time
import common_variables
from pages.base_page_object import BasePage
from locators import *


class SupplementUpsellPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.order_delay_timeout = 1

    def change_order_delay_timeout(self, timeout):
        self.order_delay_timeout = timeout

    def chose_upsell(self, upgrade, last_chance):
        if upgrade == 'yes':
            time.sleep(self.order_delay_timeout)
            self.click(YES_UPGRADE_BUTTON)
        elif upgrade == 'no':
            self.click(NO_THANKS_BUTTON)
            self.verify_downsell_popup()
            if last_chance == 'no':
                self.click(DOWNSELL_NO_THANKS_BUTTON)
            else:
                time.sleep(self.order_delay_timeout)
                button_locator = f"BUY_{last_chance.upper()}_BUTTON"
                self.click(__dict__[button_locator])

    def verify_downsell_popup(self, max_retries=5):
        for attempt in range(max_retries):
            try:
                time.sleep(1)
                self.verify_element_visible(BUY_MOST_POPULAR_BUTTON)
                break
            except:
                print(f'Failed clicking "No Thanks" button on the {attempt + 1} try! Retrying...')
                self.click(NO_THANKS_BUTTON)

        else:
            raise Exception(f'Clicking "No Thanks" button was not successful after {max_retries} retries!')

    def chose_seven_day_membership(self, decision, plan):
        self.wait_for_navigation(common_variables.restore_sleep_fourth_upsell_url, timeout=20000)
        time.sleep(0.5)
        if decision == 'accept':
            self.click(MEMBERSHIP_YES_BUTTON)
            membership_locator = f"MEMBERSHIP_{plan.upper()}_BUTTON"
            self.click(__dict__[membership_locator])
            time.sleep(1)
            self.click(ACTIVATE_MEMBERSHIP_BUTTON)
        elif decision == 'decline':
            self.click(MEMBERSHIP_NO_BUTTON)
        time.sleep(1)
        self.wait_for_navigation(common_variables.welcome_page_url)

