import time
import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage


class SupplementSalesPageLocators:
    ORDER_1_BOTTLES_BUTTON = "//*[@test-id='order-bottle-1']"
    ORDER_3_BOTTLES_BUTTON = "//*[test-id='order-bottle-3']",
    ORDER_6_BOTTLES_BUTTON = "//*[test-id='order-bottle-6']",
    FIRST_NAME_FIELD = "//input[@data-id='form-firstname']"
    LAST_NAME_FIELD = "//input[@data-id='form-lastname']"
    EMAIL_FIELD = "//input[@data-id='form-email']"
    PHONE_FIELD = "//input[@data-id='form-phone']"
    ADDRESS_FIELD = "//input[@data-id='form-address']"
    CITY_FIELD = "//input[@data-id='form-city']"
    COUNTRY_FIELD = "//input[@data-id='form-country']"
    STATE_FIELD = "//input[@data-id='form-state']"
    ZIP_FIELD = "//input[@data-id='form-zip']"
    NEXT_PAGE_ASSERT_ELEMENT = "//*[@data-id='upgrade-order']"


class SupplementStartPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def buy_bottles(self, amount):
        common_variables.supplement_funnel_email = RD.automation_template_email()
        common_variables.supplement_funnel_name = RD.automation_first_name()
        button_locator = f"ORDER_{amount}_BOTTLES_BUTTON"
        print(f'===> Buying {amount} bottle...')
        self.click(SupplementSalesPageLocators.__dict__[button_locator])
        time.sleep(2)
        self.find_element(SupplementSalesPageLocators.FIRST_NAME_FIELD).press_sequentially(common_variables.supplement_funnel_name)
        self.find_element(SupplementSalesPageLocators.LAST_NAME_FIELD).press_sequentially(RD.last_name())
        self.find_element(SupplementSalesPageLocators.EMAIL_FIELD).press_sequentially(common_variables.supplement_funnel_email)
        self.find_element(SupplementSalesPageLocators.PHONE_FIELD).press_sequentially(RD.phone_number())
        self.find_element(SupplementSalesPageLocators.ADDRESS_FIELD).press_sequentially(RD.address_line())
        self.find_element(SupplementSalesPageLocators.CITY_FIELD).press_sequentially(RD.town())
        self.find_element(SupplementSalesPageLocators.COUNTRY_FIELD).press_sequentially('USA')
        self.find_element(SupplementSalesPageLocators.STATE_FIELD).press_sequentially('CA')
        self.find_element(SupplementSalesPageLocators.ZIP_FIELD).press_sequentially(RD.postcode())
        self.populate_cc_details()
        self.wait_for_navigation(common_variables.restore_sleep_first_upsell_url, timeout=20000)
        self.verify_element_visible(SupplementSalesPageLocators.NEXT_PAGE_ASSERT_ELEMENT)
        print(f'===> Successfully bought {amount} bottle')