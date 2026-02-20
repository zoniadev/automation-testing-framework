import time
import common_functions.random_data as RD
from common_functions.url_manager import URLManager
from pages.base_page_object import BasePage
from playwright.sync_api import expect


class SupplementStartPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        
        # --- Locators ---
        self.buy_1_bottles_button = self.page.locator("*[unique-id='add-order-1-1']")
        self.buy_2_bottles_button = self.page.locator("*[unique-id='add-order-2-1']")
        self.buy_3_bottles_button = self.page.locator("*[unique-id='add-order-3-1']")
        self.buy_5_bottles_button = self.page.locator("*[unique-id='add-order-5-1']")
        self.buy_6_bottles_button = self.page.locator("*[unique-id='add-order-6-1']")
        
        self.first_name_input = self.page.locator("input[id='form-firstname']")
        self.last_name_input = self.page.locator("input[id='form-lastname']")
        self.email_input = self.page.locator("input[id='form-email']")
        self.phone_input = self.page.locator("input[id='form-phone']")
        self.address_input = self.page.locator("input[id='form-address']")
        self.city_input = self.page.locator("input[id='form-city']")
        self.country_select = self.page.locator("*[id='form-country']")
        self.state_input = self.page.locator("input[id='form-state']")
        self.zip_input = self.page.locator("input[id='form-zip']")
        
        # Upsell page locators needed for verification
        self.yes_upgrade_button = self.page.locator("*[unique-id='upgrade-order-1']")
        self.buy_most_popular_button = self.page.locator("*[data-id='add-order-3']")
        self.buy_special_offer_button = self.page.locator("*[data-id='add-order-7']")

    def get_buy_button(self, amount):
        """Returns the locator for the buy button based on bottle amount."""
        button_map = {
            '1': self.buy_1_bottles_button,
            '2': self.buy_2_bottles_button,
            '3': self.buy_3_bottles_button,
            '5': self.buy_5_bottles_button,
            '6': self.buy_6_bottles_button
        }
        if str(amount) in button_map:
            return button_map[str(amount)]
        raise ValueError(f"No buy button found for amount: {amount}")

    # --- Actions ---

    def supplement_funnel_buy_bottles(self, amount, funnel):
        self.disable_chat()
        
        # Generate and store user data in context
        self.context.test_data['email'] = RD.automation_template_email()
        self.context.test_data['name'] = RD.automation_first_name()
        
        print(f'===> Buying {amount} bottle...')
        
        if amount == '11':
            self.buy_5_bottles_button.click()
            self.buy_special_offer_button.click()
        elif amount == '5':
            self.buy_5_bottles_button.click()
            self.buy_most_popular_button.click()
        else:
            self.get_buy_button(amount).click()
            
        self.safe_fill(self.first_name_input, self.context.test_data['name'])
        self.last_name_input.fill(RD.last_name())
        self.email_input.fill(self.context.test_data['email'])
        self.phone_input.fill(RD.phone_number())
        self.address_input.fill(RD.address_line())
        self.city_input.fill(RD.town())
        
        current_funnel = self.context.test_data['funnel']
        print(f'Funnel: {current_funnel}')
        
        if current_funnel in ['restore_vision', 'restore_vision_b2g3']:
            self.country_select.select_option('USA')
        else:
            self.country_select.fill('USA')
            
        self.state_input.fill('CA')
        self.zip_input.fill(RD.postcode())
        print(f'===> User email is: {self.context.test_data["email"]}')
        
        self.populate_cc_details()
        
        next_url_key = f"{funnel.lower().replace(' ', '_')}_first_upsell_url"
        self.wait_for_navigation(URLManager.get_url(next_url_key), timeout=30000)
        
        expect(self.yes_upgrade_button).to_be_visible()
        print(f'===> Successfully bought {amount} bottle')
