import time
import common_variables
from pages.base_page_object import BasePage
from locators import *
import locators
import common_functions.random_data as RD
from playwright.sync_api import expect


class SupplementUpsellPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.order_delay_timeout = 1

    def change_order_delay_timeout(self, timeout):
        self.order_delay_timeout = timeout

    def chose_supplement_upsell(self, order, upsell_page, upgrade, last_chance):
        if upgrade == 'yes':
            print('===> Waiting to avoid payment method error...')
            time.sleep(30)
            self.context.page.locator(YES_UPGRADE_BUTTON).click()
        elif upgrade == 'no':
            self.context.page.locator(NO_THANKS_BUTTON).click()
            self.verify_downsell_popup()
            if last_chance == 'no':
                self.context.page.locator(DOWNSELL_NO_THANKS_BUTTON).click()
            else:
                print('===> Waiting to avoid payment method error...')
                time.sleep(30)
                button_locator = getattr(locators, f"BUY_{last_chance.upper()}_BUTTON")
                self.context.page.locator(button_locator).click()
        self.wait_for_navigation(self._get_supplement_next_page_url(order), timeout=30000)
        print(
            f'>>> Successfully selected upgrade "{upgrade}" and last chance "{last_chance}" for {upsell_page}')

    def _get_supplement_next_page_url(self, order):
        next_order_map = {
            'first': 'second',
            'second': 'third',
            'third': 'fourth'
        }
        next_order = next_order_map.get(order)
        if next_order:
            return getattr(common_variables, f"{common_variables.funnel}_{next_order}_upsell_url")
        else:
            raise Exception(f'Could not construct next supplement page url with given parameters:'
                            f' "{common_variables.funnel}" and "{order}"!')

    def verify_downsell_popup(self, max_retries=5):
        for attempt in range(max_retries):
            try:
                expect(self.context.page.locator(BUY_MOST_POPULAR_BUTTON)).to_be_visible()
                print('>>> Verified appearence of downsell popup')
                break
            except Exception as e:
                print(f'Failed clicking "No Thanks" button on the {attempt + 1} try! Original error: "{e}". Retrying...')
                self.context.page.locator(NO_THANKS_BUTTON).click()

        else:
            raise Exception(f'Clicking "No Thanks" button was not successful after {max_retries} retries!')

    def chose_seven_day_membership(self, decision, plan):
        if common_variables.funnel == 'restore_detox':
            next_upsell = '_third_upsell_url'
        else:
            next_upsell = '_fourth_upsell_url'
        self.wait_for_navigation(getattr(common_variables, f"{common_variables.funnel}{next_upsell}"), timeout=30000)
        if decision == 'accept':
            self.context.page.locator(MEMBERSHIP_YES_BUTTON).click()
            if plan == 'no':
                self.context.page.locator(NO_THANKS_BUTTON).click()
                self.wait_for_navigation(common_variables.welcome_page_url, timeout=30000)
            else:
                membership_locator = getattr(locators, f"MEMBERSHIP_{plan.upper()}_BUTTON")
                self.context.page.locator(membership_locator).click()
                self.retry_clicking_button(ACTIVATE_MEMBERSHIP_BUTTON, common_variables.welcome_page_url)
                # self.context.page.locator(ACTIVATE_MEMBERSHIP_BUTTON).click()
        elif decision == 'decline':
            self.retry_clicking_button(MEMBERSHIP_NO_BUTTON, common_variables.welcome_page_url)

    def chose_docuseries_booster_package_upsell(self, decision):
        print(f'>>> Selecting "{decision}" for booster package...')
        if decision != 'no':
            selection = getattr(locators, f"{decision.upper()}_PACKAGE_BUTTON")
            next_page = getattr(common_variables, f"{common_variables.funnel_prefix}_{decision.lower()}_masterclass_url")
            self.context.page.locator(selection).click()
            if decision == 'platinum':
                common_variables.docuseries_address_will_appear = True
                print('Address popup should appear next page')
        else:
            next_page = getattr(common_variables, f'{common_variables.funnel_prefix}_masterclass_url')
            self.context.page.locator(NO_THANKS_BUTTON).click()
        self.wait_for_navigation(next_page, timeout=30000)
        print(f'>>> Successfully selected "{decision}" for booster package')
        if decision == 'platinum':
            self.populate_shipping_address()


    def chose_docuseries_masterclass_upsell(self, decision):
        print(f'>>> Selecting "{decision}" for masterclass...')
        if common_variables.funnel_prefix in ['lg', 'is']:
            upsell3 = 'restore_life'
        elif common_variables.funnel_prefix in ['km', 'twl', 'cr']:
            upsell3 = 'restore_sleep'
        else:
            upsell3 = 'restore_detox'
        self._maybe_populate_shipping_address()
        if decision != 'no':
            print('===> Waiting a bit to avoid payment method error...')
            time.sleep(10)
            self.context.page.locator(BUY_MASTERCLASS_BUTTON).click()
            next_page = getattr(common_variables, f'{common_variables.funnel_prefix}_{upsell3}_bought_url')
        else:
            self.context.page.locator(SKIP_MASTERCLASS_BUTTON).click()
            next_page = getattr(common_variables, f'{common_variables.funnel_prefix}_{upsell3}_not_bought_url')
        self.wait_for_navigation(next_page, timeout=30000)
        print(f'>>> Successfully selected "{decision}" for masterclass')

    def _get_docuseries_next_page_navigation(self, upsell_page):
        """Determines the next page URL based on the upsell page and funnel."""
        funnel_prefix = common_variables.funnel_prefix
        if upsell_page == 'Restore Detox':
            if funnel_prefix in ['lg', 'km', 'is', 'twl', 'pc']:
                return common_variables.welcome_page_url
            else:
                page_url = f'{funnel_prefix}_restore_life_url'
                return getattr(common_variables, page_url)
        elif upsell_page == 'Restore Life':
            if funnel_prefix in ['lg', 'is']:
                page_url = f'{funnel_prefix}_restore_detox_url'
                return getattr(common_variables, page_url)
            else:
                return common_variables.welcome_page_url
        elif upsell_page == 'Restore Sleep':
            if funnel_prefix in ['cr']:
                page_url = f'{funnel_prefix}_restore_life_url'
            else:
                page_url = f'{funnel_prefix}_restore_detox_url'
            return getattr(common_variables, page_url)

    def _handle_docuseries_bottle_purchase(self, upsell_page, amount, next_page_navigation):
        """Handles the logic for purchasing (or not purchasing) bottles."""
        if amount == 'no':
            print('===> Not buying bottles...')
            if common_variables.funnel_prefix != 'pc':
                next_page = getattr(common_variables, f"{common_variables.funnel_prefix}_{upsell_page.lower().replace(' ', '_')}_downsell_url")
            else:
                next_page = next_page_navigation
            self.retry_clicking_button(NO_THANKS_BUTTON, next_page)
        else:
            print(f'===> Buying {amount} bottle...')
            next_page = getattr(common_variables, f"{common_variables.funnel_prefix}_{upsell_page.lower().replace(' ', '_')}_upsell_url")
            button_locator = getattr(locators, f"BUY_{amount}_BOTTLES_BUTTON")
            print('===> Waiting to avoid payment method error...')
            time.sleep(30)
            self.retry_clicking_button(button_locator, next_page)
            print(f'===> Successfully bought {amount} bottle/s')
            common_variables.docuseries_address_will_appear = True
            print('Address popup should appear next page')

    def _handle_docuseries_upsell_downsell(self, amount, upsell_downsell):
        """Handles the logic for the upsell/downsell decision."""
        funnel_prefix = common_variables.funnel_prefix
        if upsell_downsell == 'upgrade':
            print('===> Waiting to avoid payment method error...')
            time.sleep(30)
            self.context.page.locator(YES_UPGRADE_BUTTON).click()
            print('===> Upgrading order...')
            common_variables.docuseries_address_will_appear = True
            print('Address popup should appear next page')
        elif upsell_downsell == 'no':
            if funnel_prefix == 'pc':
                if amount != 'no':
                    self.context.page.locator(NO_THANKS_BUTTON).click()
            else:
                self.context.page.locator(NO_THANKS_BUTTON).click()
                if amount != 'no':
                    self.context.page.locator(DOWNSELL_NO_THANKS_BUTTON).click()
                    print('===> Not upgrading...')
        elif upsell_downsell in ['best_value', 'most_popular']:
            if funnel_prefix != 'pc':
                self.context.page.locator(NO_THANKS_BUTTON).click()
                if upsell_downsell == 'best_value':
                    self.context.page.locator(BUY_BEST_VALUE_BUTTON).click()
                else:
                    self.context.page.locator(BUY_MOST_POPULAR_BUTTON).click()
                print(f'===> Not upgrading, but getting {upsell_downsell} downsell...')

    def _maybe_populate_shipping_address(self):
        """Populates shipping address if the flag is set."""
        if common_variables.docuseries_address_will_appear:
            self.populate_shipping_address()

    def docuseries_buy_upsells(self, upsell_page, amount, upsell_downsell):
        """Orchestrates the process of buying docuseries upsells."""
        print(f'>>> Selecting "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}...')
        next_page_navigation = self._get_docuseries_next_page_navigation(upsell_page)
        self._maybe_populate_shipping_address()
        if upsell_downsell not in ['upgrade', 'no', 'best_value', 'most_popular']:
            raise Exception(f'Unsupported "upsell_downsell" value: {upsell_downsell}')
        self._handle_docuseries_bottle_purchase(upsell_page, amount, next_page_navigation)
        self._maybe_populate_shipping_address()
        self._handle_docuseries_upsell_downsell(amount, upsell_downsell)
        self._maybe_populate_shipping_address()
        self.wait_for_navigation(next_page_navigation, timeout=30000)
        print(f'>>> Successfully selected "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}')

    def _verify_shipping_popup(self):
        """Verifies the shipping popup is visible and has the correct title."""
        expected_title = "Please enter below your shipping address where we can ship your supplement."
        modal_title = self.context.page.locator(SHIPPING_POPUP_TITLE)
        actual_title = modal_title.text_content()
        assert actual_title.strip() == expected_title, (
            f"Popup title mismatch! Expected: '{expected_title}', Actual: '{actual_title.strip()}'"
        )
        expect(self.context.page.locator(SHIPPING_FULL_NAME_FIELD)).to_be_visible(timeout=10000)
        assert self.context.page.locator(SHIPPING_FULL_NAME_FIELD).get_attribute("placeholder") == "First and Last Names*"

    def _get_shipping_locators(self):
        """Returns the correct set of locators based on the current URL and funnel."""
        url = self.context.page.url
        funnel = common_variables.funnel
        if 'rl' in url or 'life' in url:
            if funnel in ['tf_ev', 'bb_live', 'bb_ev', 'lg_ev', 'lg_live', 'cr_live', 'cr_bonus', 'cr_ev', 'cr_1ep']:
                return SHIPPING_PHONE_FIELD_ALT, SHIPPING_ADDRESS_FIELD_ALT, SHIPPING_CITY_FIELD_ALT, SHIPPING_STATE_FIELD_ALT, SHIPPING_ZIP_FIELD_ALT, SHIPPING_COUNTRY_FIELD_ALT
            else:
                return SHIPPING_PHONE_FIELD_ALT2, SHIPPING_ADDRESS_FIELD_ALT2, SHIPPING_CITY_FIELD_ALT2, SHIPPING_STATE_FIELD_ALT2, SHIPPING_ZIP_FIELD_ALT2, SHIPPING_COUNTRY_FIELD_ALT2
        elif 'rd' in url or 'detox' in url or 'welcome' in url:
            return SHIPPING_PHONE_FIELD_ALT, SHIPPING_ADDRESS_FIELD_ALT, SHIPPING_CITY_FIELD_ALT, SHIPPING_STATE_FIELD_ALT, SHIPPING_ZIP_FIELD_ALT, SHIPPING_COUNTRY_FIELD_ALT
        else:
            return SHIPPING_PHONE_FIELD, SHIPPING_ADDRESS_FIELD, SHIPPING_CITY_FIELD, SHIPPING_STATE_FIELD, SHIPPING_ZIP_FIELD, SHIPPING_COUNTRY_FIELD

    def _fill_shipping_form(self, locators):
        """Fills the shipping form using the provided locators."""
        phone_locator, address_locator, city_locator, state_locator, zip_locator, country_locator = locators
        self.context.page.locator(SHIPPING_FULL_NAME_FIELD).fill(common_variables.supplement_funnel_name)
        self.context.page.locator(phone_locator).fill(RD.phone_number())
        self.context.page.locator(address_locator).fill(RD.address_line())
        self.context.page.locator(city_locator).fill(RD.town())
        self.context.page.locator(state_locator).fill(RD.state())
        self.context.page.locator(zip_locator).fill(RD.postcode())
        self.context.page.locator(country_locator).fill('USA')
        self.context.page.locator(SHIPPING_SUBMIT_BUTTON).click()

    def populate_shipping_address(self):
        """Orchestrates the process of populating the shipping address."""
        if not common_variables.docuseries_address_already_filled:
            print('>>>Entering shipping details...')
            self._verify_shipping_popup()
            locators_to_use = self._get_shipping_locators()
            self._fill_shipping_form(locators_to_use)
            print('>>>Successfully entered shipping details')
            common_variables.docuseries_address_already_filled = True

    def retry_clicking_button(self, button, next_page):
        self.context.page.locator(button).click()
        try:
            self.wait_for_navigation(next_page, timeout=15000)
        except Exception as E:
            print(f'===> Issue with clicking button "{button}", page was not changed to {next_page}, retrying...')
            print(f'Error: {E}')
            self.context.page.locator(button).click()
            self.wait_for_navigation(next_page, timeout=30000)
            print('===> Second try was successful')
