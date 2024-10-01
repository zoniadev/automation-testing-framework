import time
import common_variables
from pages.base_page_object import BasePage
from locators import *
import locators
import common_functions.random_data as RD


class SupplementUpsellPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.order_delay_timeout = 1

    def change_order_delay_timeout(self, timeout):
        self.order_delay_timeout = timeout

    def chose_supplement_upsell(self, upsell_page, upgrade, last_chance):
        if upsell_page == '6 More bottles of Restore Sleep':
            next_page_navigation = common_variables.restore_sleep_second_upsell_url
        elif upsell_page == 'Restore Life':
            next_page_navigation = common_variables.restore_sleep_third_upsell_url
        elif upsell_page == 'Restore Detox':
            next_page_navigation = common_variables.restore_sleep_fourth_upsell_url
        if upgrade == 'yes':
            time.sleep(self.order_delay_timeout)
            self.click(YES_UPGRADE_BUTTON)
        elif upgrade == 'no':
            time.sleep(1)
            self.click(NO_THANKS_BUTTON)
            self.verify_downsell_popup()
            if last_chance == 'no':
                self.click(DOWNSELL_NO_THANKS_BUTTON)
            else:
                time.sleep(self.order_delay_timeout)
                button_locator = getattr(locators, f"BUY_{last_chance.upper()}_BUTTON")
                self.click(button_locator)
        self.wait_for_navigation(next_page_navigation, timeout=20000)
        print(
            f'>>> Successfully selected upgrade "{upgrade}" and last chance "{last_chance}" for {upsell_page}')

    def verify_downsell_popup(self, max_retries=5):
        for attempt in range(max_retries):
            try:
                time.sleep(1)
                self.verify_element_visible(BUY_MOST_POPULAR_BUTTON)
                print('>>> Verified appearence of downsell popup')
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
            time.sleep(0.5)
            self.click(selection)
        else:
            next_page = common_variables.unbroken_masterclass_url
            time.sleep(0.5)
            self.click(NO_THANKS_BUTTON)
        self.wait_for_navigation(next_page, timeout=20000)
        print(f'>>> Successfully selected "{decision}" for booster package')
        if decision == 'platinum':
            self.populate_shipping_address()
            common_variables.docuseries_address_already_filled = True


    def chose_docuseries_masterclass_upsell(self, decision):
        print(f'>>> Selecting "{decision}" for masterclass...')
        if decision != 'no':
            time.sleep(0.5)
            self.click(BUY_MASTERCLASS_BUTTON)
            next_page = common_variables.unbroken_restore_detox_bought_url
        else:
            time.sleep(0.5)
            self.click(SKIP_MASTERCLASS_BUTTON)
            next_page = common_variables.unbroken_restore_detox_not_bought_url
        self.wait_for_navigation(next_page, timeout=20000)
        print(f'>>> Successfully selected "{decision}" for masterclass')

    def docuseries_buy_upsells(self, upsell_page, amount, upsell_downsell):
        if upsell_page == 'Restore Detox':
            next_page_navigation = common_variables.unbroken_restore_life_url
        elif upsell_page == 'Restore Life':
            next_page_navigation = common_variables.welcome_page_url
            if amount != 'no':
                self.change_order_delay_timeout(30)
        print(f'>>> Selecting "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}...')
        if upsell_downsell not in ['upgrade', 'no', 'best_value', 'most_popular']:
            raise Exception(f'Unsupported "upsell_downsell" value: {upsell_downsell}')
        if amount == 'no':
            print('===> Not buying bottles...')
            next_page = getattr(common_variables, f"unbroken_{upsell_page.lower().replace(' ', '_')}_downsell_url")
            time.sleep(0.5)
            self.retry_clicking_button(NO_THANKS_BUTTON, next_page)
        else:
            print(f'===> Buying {amount} bottle...')
            next_page = getattr(common_variables, f"unbroken_{upsell_page.lower().replace(' ', '_')}_upsell_url")
            button_locator = getattr(locators, f"BUY_{amount}_BOTTLES_BUTTON")
            time.sleep(self.order_delay_timeout)
            self.retry_clicking_button(button_locator, next_page)
            time.sleep(0.5)
            print(f'===> Successfully bought {amount} bottle')
            if not common_variables.docuseries_address_already_filled:
                self.populate_shipping_address()
        time.sleep(0.5)
        if upsell_downsell == 'upgrade':
            time.sleep(0.5)
            self.click(YES_UPGRADE_BUTTON)
            print('===> Upgrading order...')
        elif upsell_downsell == 'no':
            self.click(NO_THANKS_BUTTON)
            time.sleep(1)
            if amount != 'no':
                self.click(DOWNSELL_NO_THANKS_BUTTON)
                print('===> Not upgrading...')
        else:
            self.click(NO_THANKS_BUTTON)
            time.sleep(0.5)
            if upsell_downsell == 'best_value':
                time.sleep(0.5)
                self.click(BUY_BEST_VALUE_BUTTON)
            else:
                time.sleep(0.5)
                self.click(BUY_MOST_POPULAR_BUTTON)
            print(f'===> Not upgrading, but getting {upsell_downsell} downsell...')
        self.wait_for_navigation(next_page_navigation, timeout=20000)
        print(f'>>> Successfully selected "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}')

    def populate_shipping_address(self):
        print('>>>Entering shipping details...')
        time.sleep(1)
        self.enter_text(SHIPPING_FULL_NAME_FIELD, common_variables.supplement_funnel_name)
        self.enter_text(SHIPPING_PHONE_FIELD, RD.phone_number())
        self.enter_text(SHIPPING_ADDRESS_FIELD, RD.address_line())
        self.enter_text(SHIPPING_CITY_FIELD, RD.town())
        self.enter_text(SHIPPING_STATE_FIELD, RD.state())
        self.enter_text(SHIPPING_ZIP_FIELD, RD.postcode())
        self.enter_text(SHIPPING_COUNTRY_FIELD, 'USA')
        self.click(SHIPPING_SUBMIT_BUTTON)
        time.sleep(0.5)
        print('>>>Successfully entered shipping details')
        common_variables.docuseries_address_already_filled = True

    def retry_clicking_button(self, button, next_page):
        self.click(button)
        try:
            self.wait_for_navigation(next_page, timeout=5000)
        except:
            print(f'===> Issue with clicking button "{button}", retrying...')
            self.click(button)
            time.sleep(0.5)
            self.wait_for_navigation(next_page, timeout=20000)
            print('===> Second try was successful')
