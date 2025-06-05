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

    def chose_supplement_upsell(self, order, upsell_page, upgrade, last_chance):
        if upgrade == 'yes':
            print('===> Waiting to avoid payment method error...')
            time.sleep(30)
            self.click(YES_UPGRADE_BUTTON)
        elif upgrade == 'no':
            time.sleep(1)
            self.click(NO_THANKS_BUTTON)
            self.verify_downsell_popup()
            if last_chance == 'no':
                self.click(DOWNSELL_NO_THANKS_BUTTON)
            else:
                print('===> Waiting to avoid payment method error...')
                time.sleep(30)
                button_locator = getattr(locators, f"BUY_{last_chance.upper()}_BUTTON")
                self.click(button_locator)
        self.wait_for_navigation(self.get_supplement_next_page_url(order), timeout=30000)
        print(
            f'>>> Successfully selected upgrade "{upgrade}" and last chance "{last_chance}" for {upsell_page}')

    def get_supplement_next_page_url(self, order):
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
                time.sleep(1)
                self.verify_element_visible(BUY_MOST_POPULAR_BUTTON)
                print('>>> Verified appearence of downsell popup')
                break
            except Exception as e:
                print(f'Failed clicking "No Thanks" button on the {attempt + 1} try! Original error: "{e}". Retrying...')
                self.click(NO_THANKS_BUTTON)

        else:
            raise Exception(f'Clicking "No Thanks" button was not successful after {max_retries} retries!')

    def chose_seven_day_membership(self, decision, plan):
        self.wait_for_navigation(getattr(common_variables, f"{common_variables.funnel}_fourth_upsell_url"), timeout=30000)
        time.sleep(5)
        if decision == 'accept':
            self.click(MEMBERSHIP_YES_BUTTON)
            if plan == 'no':
                self.click(NO_THANKS_BUTTON)
            else:
                membership_locator = getattr(locators, f"MEMBERSHIP_{plan.upper()}_BUTTON")
                self.click(membership_locator)
                time.sleep(2)
                self.click(ACTIVATE_MEMBERSHIP_BUTTON)
        elif decision == 'decline':
            self.click(MEMBERSHIP_NO_BUTTON)
        time.sleep(1)
        self.wait_for_navigation(common_variables.welcome_page_url, timeout=30000)

    def chose_docuseries_booster_package_upsell(self, decision):
        print(f'>>> Selecting "{decision}" for booster package...')
        if decision != 'no':
            selection = getattr(locators, f"{decision.upper()}_PACKAGE_BUTTON")
            next_page = getattr(common_variables, f"{common_variables.funnel_prefix}_{decision.lower()}_masterclass_url")
            time.sleep(0.5)
            self.click(selection)
            if decision == 'platinum':
                common_variables.docuseries_address_will_appear = True
                print('Address popup should appear next page')
        else:
            next_page = getattr(common_variables, f'{common_variables.funnel_prefix}_masterclass_url')
            time.sleep(0.5)
            self.click(NO_THANKS_BUTTON)
        self.wait_for_navigation(next_page, timeout=30000)
        print(f'>>> Successfully selected "{decision}" for booster package')
        if decision == 'platinum':
            self.populate_shipping_address()


    def chose_docuseries_masterclass_upsell(self, decision):
        print(f'>>> Selecting "{decision}" for masterclass...')
        if common_variables.funnel_prefix in ['lg', 'is']:
            upsell3 = 'restore_life'
        elif common_variables.funnel_prefix == 'km':
            upsell3 = 'restore_sleep'
        else:
            upsell3 = 'restore_detox'
        if common_variables.docuseries_address_will_appear:
            self.populate_shipping_address()
        if decision != 'no':
            print('===> Waiting a bit to avoid payment method error...')
            time.sleep(10)
            self.click(BUY_MASTERCLASS_BUTTON)
            next_page = getattr(common_variables, f'{common_variables.funnel_prefix}_{upsell3}_bought_url')
        else:
            time.sleep(0.5)
            self.click(SKIP_MASTERCLASS_BUTTON)
            next_page = getattr(common_variables, f'{common_variables.funnel_prefix}_{upsell3}_not_bought_url')
        self.wait_for_navigation(next_page, timeout=30000)
        print(f'>>> Successfully selected "{decision}" for masterclass')

    def docuseries_buy_upsells(self, upsell_page, amount, upsell_downsell):
        if upsell_page == 'Restore Detox':
            if common_variables.funnel_prefix in ['lg', 'km', 'is']:
                next_page_navigation = common_variables.welcome_page_url
            else:
                page_url = f'{common_variables.funnel_prefix}_restore_life_url'
                next_page_navigation = getattr(common_variables, page_url)
        elif upsell_page == 'Restore Life':
            if common_variables.funnel_prefix in ['lg', 'is']:
                page_url = f'{common_variables.funnel_prefix}_restore_detox_url'
                next_page_navigation = getattr(common_variables, page_url)
            else:
                next_page_navigation = common_variables.welcome_page_url
        elif upsell_page == 'Restore Sleep':
            page_url = f'{common_variables.funnel_prefix}_restore_detox_url'
            next_page_navigation = getattr(common_variables, page_url)
        print(f'>>> Selecting "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}...')
        if common_variables.docuseries_address_will_appear:
            self.populate_shipping_address()
        if upsell_downsell not in ['upgrade', 'no', 'best_value', 'most_popular']:
            raise Exception(f'Unsupported "upsell_downsell" value: {upsell_downsell}')
        if amount == 'no':
            print('===> Not buying bottles...')
            next_page = getattr(common_variables, f"{common_variables.funnel_prefix}_{upsell_page.lower().replace(' ', '_')}_downsell_url")
            time.sleep(0.5)
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
        time.sleep(0.5)
        if common_variables.docuseries_address_will_appear:
            self.populate_shipping_address()
        if upsell_downsell == 'upgrade':
            print('===> Waiting to avoid payment method error...')
            time.sleep(30)
            self.click(YES_UPGRADE_BUTTON)
            print('===> Upgrading order...')
            common_variables.docuseries_address_will_appear = True
            print('Address popup should appear next page')
        elif upsell_downsell == 'no':
            self.click(NO_THANKS_BUTTON)
            time.sleep(1)
            if amount != 'no':
                self.click(DOWNSELL_NO_THANKS_BUTTON)
                print('===> Not upgrading...')
        else:
            self.click(NO_THANKS_BUTTON)
            time.sleep(1)
            if upsell_downsell == 'best_value':
                time.sleep(1)
                self.click(BUY_BEST_VALUE_BUTTON)
            else:
                time.sleep(1)
                self.click(BUY_MOST_POPULAR_BUTTON)
            print(f'===> Not upgrading, but getting {upsell_downsell} downsell...')
        if common_variables.docuseries_address_will_appear:
            self.populate_shipping_address()
        self.wait_for_navigation(next_page_navigation, timeout=30000)
        print(f'>>> Successfully selected "{amount}" bottles and "{upsell_downsell}" in upsell/downsell for {upsell_page}')


    def populate_shipping_address(self):
        if not common_variables.docuseries_address_already_filled:
            expected_shipping_popup_title = "Please enter below your shipping address where we can ship your supplement."
            print('>>>Entering shipping details...')
            time.sleep(10)
            modal_title = self.find_not_unique_element(SHIPPING_POPUP_TITLE)
            actual_title = modal_title.text_content()
            print(f'Actual title: {actual_title}')
            assert actual_title.strip() == expected_shipping_popup_title, (f"Popup title mismatch! Expected:"
                                                                           f" '{expected_shipping_popup_title}', "
                                                                           f"Actual: '{actual_title.strip()}'")
            self.verify_element_visible(SHIPPING_FULL_NAME_FIELD)
            self.enter_text(SHIPPING_FULL_NAME_FIELD, common_variables.supplement_funnel_name)
            url = self.context.page.url
            if 'rl' in url or 'life' in url:
                self.enter_text(SHIPPING_PHONE_FIELD_ALT2, RD.phone_number())
                self.enter_text(SHIPPING_ADDRESS_FIELD_ALT2, RD.address_line())
                self.enter_text(SHIPPING_CITY_FIELD_ALT2, RD.town())
                self.enter_text(SHIPPING_STATE_FIELD_ALT2, RD.state())
                self.enter_text(SHIPPING_ZIP_FIELD_ALT2, RD.postcode())
                self.enter_text(SHIPPING_COUNTRY_FIELD_ALT2, 'USA')
            elif 'rd' in url or 'detox' in url:
                self.enter_text(SHIPPING_PHONE_FIELD_ALT, RD.phone_number())
                self.enter_text(SHIPPING_ADDRESS_FIELD_ALT, RD.address_line())
                self.enter_text(SHIPPING_CITY_FIELD_ALT, RD.town())
                self.enter_text(SHIPPING_STATE_FIELD_ALT, RD.state())
                self.enter_text(SHIPPING_ZIP_FIELD_ALT, RD.postcode())
                self.enter_text(SHIPPING_COUNTRY_FIELD_ALT, 'USA')
            else:
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
        except Exception as E:
            print(f'===> Issue with clicking button "{button}", page was not changed to {next_page}, retrying...')
            print(f'Error: {E}')
            self.click(button)
            time.sleep(0.5)
            self.wait_for_navigation(next_page, timeout=30000)
            print('===> Second try was successful')
