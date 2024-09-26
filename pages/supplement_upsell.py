import time
import common_variables
from pages.base_page_object import BasePage
from locators import *
import locators


class SupplementUpsellPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.order_delay_timeout = 1

    def change_order_delay_timeout(self, timeout):
        self.order_delay_timeout = timeout

    def chose_supplement_upsell(self, upgrade, last_chance, docuseries=True):
        if upgrade == 'yes':
            time.sleep(self.order_delay_timeout)
            self.click(YES_UPGRADE_BUTTON)
        elif upgrade == 'no':
            time.sleep(0.5)
            self.click(NO_THANKS_BUTTON)
            self.verify_downsell_popup()
            if last_chance == 'no':
                self.click(DOWNSELL_NO_THANKS_BUTTON)
            else:
                time.sleep(self.order_delay_timeout)
                button_locator = getattr(locators, f"BUY_{last_chance.upper()}_BUTTON")
                self.click(button_locator)

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
            membership_locator = getattr(locators, f"MEMBERSHIP_{plan.upper()}_BUTTON")
            self.click(membership_locator)
            time.sleep(1)
            self.click(ACTIVATE_MEMBERSHIP_BUTTON)
        elif decision == 'decline':
            self.click(MEMBERSHIP_NO_BUTTON)
        time.sleep(1)
        self.wait_for_navigation(common_variables.welcome_page_url, timeout=20000)

    def chose_docuseries_booster_package_upsell(self, decision):
        print(f'>>> Selecting "{decision}" for booster package...')
        if decision != 'no':
            selection = getattr(locators, f"{decision.upper()}_PACKAGE_BUTTON")
            next_page = getattr(common_variables, f"unbroken_{decision.lower()}_masterclass_url")
            time.sleep(self.order_delay_timeout)
            self.click(selection)
        else:
            next_page = common_variables.unbroken_masterclass_url
            time.sleep(0.5)
            self.click(NO_THANKS_BUTTON)
        self.wait_for_navigation(next_page, timeout=20000)
        print(f'>>> Successfully selected "{decision}" for booster package')


    def chose_docuseries_masterclass_upsell(self, decision):
        print(f'>>> Selecting "{decision}" for masterclass...')
        if decision != 'no':
            time.sleep(self.order_delay_timeout)
            self.click(BUY_MASTERCLASS_BUTTON)
            next_page = common_variables.unbroken_restore_detox_bought_url
        else:
            time.sleep(0.5)
            self.click(SKIP_MASTERCLASS_BUTTON)
            next_page = common_variables.unbroken_restore_detox_not_bought_url
        self.wait_for_navigation(next_page, timeout=20000)
        print(f'>>> Successfully selected "{decision}" for masterclass')

    def docuseries_buy_bottles(self, upsell_page, amount, upsell_downsell):
        print(f'>>> Selecting "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}...')
        if upsell_downsell not in ['upgrade', 'no', 'best_value', 'most_popular']:
            raise Exception(f'Unsupported "upsell_downsell" value: {upsell_downsell}')
        if amount == 'no':
            print('===> Not buying bottles...')
            next_page = common_variables.unbroken_restore_detox_downsell_url
            time.sleep(0.5)
            self.click(NO_THANKS_BUTTON)
        else:
            print(f'===> Buying {amount} bottle...')
            next_page = common_variables.unbroken_restore_detox_upsell_url
            button_locator = getattr(locators, f"BUY_{amount}_BOTTLES_BUTTON")
            self.click(button_locator)
            time.sleep(0.5)
            print(f'===> Successfully bought {amount} bottle')
        self.wait_for_navigation(next_page, timeout=20000)
        if upsell_downsell == 'upgrade':
            self.click(YES_UPGRADE_BUTTON)
            print('===> Upgrading order...')
        elif upsell_downsell == 'no':
            self.click(NO_THANKS_BUTTON)
            time.sleep(0.5)
            self.click(DOWNSELL_NO_THANKS_BUTTON)
            print('===> Not upgrading...')
        else:
            self.click(NO_THANKS_BUTTON)
            time.sleep(0.5)
            if upsell_downsell == 'best_value':
                self.click(BUY_BEST_VALUE_BUTTON)
            else:
                self.click(BUY_MOST_POPULAR_BUTTON)
            print(f'===> Not upgrading, but getting {upsell_downsell} downsell...')
            self.wait_for_navigation(common_variables.unbroken_restore_life_url, timeout=20000)
            print(f'>>> Successfully selected "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}')




