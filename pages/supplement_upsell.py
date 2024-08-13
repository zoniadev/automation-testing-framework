import time
import common_variables
from pages.base_page_object import BasePage


class SupplementUpsellPageLocators:
    YES_UPGRADE_BUTTON = "//*[@data-id='upgrade-order']"
    NO_THANKS_BUTTON = "//*[@data-id='no-thanks']"
    DOWNSELL_NO_THANKS_BUTTON = "//*[@data-id='downsell-no-thanks']"
    BUY_BEST_VALUE_BUTTON = "//*[@data-id='add-order-6']"
    BUY_MOST_POPULAR_BUTTON = "//*[@data-id='add-order-3']"
    MEMBERSHIP_YES_BUTTON = "//*[@id='register-top-btn']"
    MEMBERSHIP_NO_BUTTON = "//*[@id='skip-registration-top']"
    MEMBERSHIP_MONTHLY_BUTTON = "//*[@data-plan='monthly_new']"
    MEMBERSHIP_QUARTERLY_BUTTON = "//*[@data-plan='quarterly']"
    MEMBERSHIP_ANNUAL_BUTTON = "//*[@data-plan='yearly_new']"
    ACTIVATE_MEMBERSHIP_BUTTON = "//*[@id='register-middle']"


class SupplementUpsellPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.order_delay_timeout = 1

    def chose_upsell(self, upgrade, last_chance):
        if upgrade == 'yes':
            time.sleep(self.order_delay_timeout)
            self.click(SupplementUpsellPageLocators.YES_UPGRADE_BUTTON)
        elif upgrade == 'no':
            self.click(SupplementUpsellPageLocators.NO_THANKS_BUTTON)
            self.verify_downsell_popup()
            if last_chance == 'no':
                self.click(SupplementUpsellPageLocators.DOWNSELL_NO_THANKS_BUTTON)
            else:
                time.sleep(self.order_delay_timeout)
                button_locator = f"BUY_{last_chance.upper()}_BUTTON"
                self.click(SupplementUpsellPageLocators.__dict__[button_locator])

    def verify_downsell_popup(self, max_retries=5):
        for attempt in range(max_retries):
            try:
                time.sleep(1)
                self.verify_element_visible(SupplementUpsellPageLocators.BUY_MOST_POPULAR_BUTTON)
                break
            except:
                print(f'Failed clicking "No Thanks" button on the {attempt + 1} try! Retrying...')
                self.click(SupplementUpsellPageLocators.NO_THANKS_BUTTON)

        else:
            raise Exception(f'Clicking "No Thanks" button was not successful after {max_retries} retries!')

    def chose_seven_day_membership(self, decision, plan):
        self.wait_for_navigation(common_variables.restore_sleep_fourth_upsell_url, timeout=20000)
        time.sleep(0.5)
        if decision == 'accept':
            self.click(SupplementUpsellPageLocators.MEMBERSHIP_YES_BUTTON)
            membership_locator = f"MEMBERSHIP_{plan.upper()}_BUTTON"
            self.click(SupplementUpsellPageLocators.__dict__[membership_locator])
            time.sleep(1)
            self.click(SupplementUpsellPageLocators.ACTIVATE_MEMBERSHIP_BUTTON)
        elif decision == 'decline':
            self.click(SupplementUpsellPageLocators.MEMBERSHIP_NO_BUTTON)
        time.sleep(1)
        self.wait_for_navigation(common_variables.welcome_page_url)

