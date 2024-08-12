import time
import common_functions.random_data as RD
from pages.base_page_object import BasePage


class RestoreSleepPageLocators:
    ORDER_1_BOTTLES_BUTTON = "//*[@test-id='order-bottle-1']"
    ORDER_3_BOTTLES_BUTTON = "//*[test-id='order-bottle-3']",
    ORDER_6_BOTTLES_BUTTON = "//*[test-id='order-bottle-6']",
    FIRST_NAME_FIELD = "//input[@id='form-firstname']"
    LAST_NAME_FIELD = "//input[@id='form-lastname']"
    EMAIL_FIELD = "//input[@id='form-email']"
    PHONE_FIELD = "//input[@id='form-phone']"
    ADDRESS_FIELD = "//input[@id='form-address']"
    CITY_FIELD = "//input[@id='form-city']"
    COUNTRY_FIELD = "//input[@id='form-country']"
    STATE_FIELD = "//input[@id='form-state']"
    ZIP_FIELD = "//input[@id='form-zip']"
    NEXT_PAGE_ASSERT_ELEMENT = "//*[contains(text(), 'YES, Upgrade My Order')]"


class RestoreSleepPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def buy_bottles(self, amount):
        button_locator = f"ORDER_{amount}_BOTTLES_BUTTON"
        print(f'===> Buying {amount} bottle...')
        self.find_element(RestoreSleepPageLocators.__dict__[button_locator]).click()
        time.sleep(1)
        self.find_element(RestoreSleepPageLocators.FIRST_NAME_FIELD).press_sequentially(RD.first_name())
        self.find_element(RestoreSleepPageLocators.LAST_NAME_FIELD).press_sequentially(RD.last_name())
        self.find_element(RestoreSleepPageLocators.EMAIL_FIELD).press_sequentially(RD.automation_template_email())
        self.find_element(RestoreSleepPageLocators.PHONE_FIELD).press_sequentially(RD.phone_number())
        self.find_element(RestoreSleepPageLocators.ADDRESS_FIELD).press_sequentially(RD.address_line())
        self.find_element(RestoreSleepPageLocators.CITY_FIELD).press_sequentially(RD.town())
        self.find_element(RestoreSleepPageLocators.COUNTRY_FIELD).press_sequentially('USA')
        self.find_element(RestoreSleepPageLocators.STATE_FIELD).press_sequentially('CA')
        self.find_element(RestoreSleepPageLocators.ZIP_FIELD).press_sequentially(RD.postcode())
        self.populate_cc_details()
        self.verify_element_visible(RestoreSleepPageLocators.NEXT_PAGE_ASSERT_ELEMENT)
        print(f'===> Successfully bought {amount} bottle')