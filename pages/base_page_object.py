import re
import time
from playwright.sync_api import Page, expect
import common_variables


class BasePageLocators:
    PLACE_ORDER_BUTTON = "//button[@data-id='order-btn']"
    CC_NUM_FRAME = '//iframe[@id="braintree-hosted-field-number"]'
    CC_NUM_FIELD = 'Card Number'
    CC_EXP_DATE_FRAME = '//iframe[@id="braintree-hosted-field-expirationDate"]'
    CC_EXP_DATE_FIELD = 'Expiration Date(MM/YY)'
    CC_CVV_FRAME = '//iframe[@id="braintree-hosted-field-cvv"]'
    CC_CVV_FIELD = 'Security Code(CCV)'
    CC_ZIP_FRAME = '//iframe[@id="braintree-hosted-field-postalCode"]'
    CC_ZIP_FIELD = 'Billing Zip/Postal Code'


class BasePage(object):
    __TIMEOUT = 15000

    def __init__(self, context):
        self.context = context

    def find_element(self, locator):
        elements = self.context.page.locator(locator).all()
        if not elements:
            raise Exception(f'No elements found with locator {locator}!')
        visible_elements = [element for element in elements if element.is_visible()]
        if not visible_elements:
            raise Exception(f'No visible elements found with locator {locator}!')
        visible_elements_amount = len(visible_elements)
        if visible_elements_amount == 1:
            print(f'===> One visible element with "{locator}" found from total {len(elements)}')
            return visible_elements[0]
        else:
            print(f'===> {visible_elements_amount} visible elements with "{locator}" found from total {len(elements)}.')
            return visible_elements[1]

    def verify_element_visible(self, locator):
        expect(self.find_element(locator)).to_be_visible()
        print(f'===> Verified element "{locator}" is visible')

    def click(self, locator):
        element = self.find_element(locator)
        element.scroll_into_view_if_needed()
        element.click()
        print(f'===> Clicked element "{locator}"')

    def wait_for_navigation(self, url, timeout=__TIMEOUT):
        print(f'===> Waiting for URL starting with "{url}"')
        # self.context.page.wait_for_url(f"**/{url}/**", timeout=timeout)
        expect(self.context.page).to_have_url(re.compile(f"^{url}.*"))
        print(f'===> URL successfully changed to "{url}"')

    def get_text(self, locator):
        print(f'===> Getting text from element "{locator}"...')
        return self.find_element(locator).text_content()

    def verify_element_contain_text(self, locator, expected_text):
        expect(self.find_element(locator)).to_have_text(expected_text)


    def retry_cc_number_entry(self, max_retries=5):
        cc_number = self.context.page.frame_locator(BasePageLocators.CC_NUM_FRAME).get_by_placeholder(BasePageLocators.CC_NUM_FIELD)
        for attempt in range(max_retries):
            try:
                cc_number.fill("")
                cc_number.press_sequentially(common_variables.test_cc_number, delay=50)
                time.sleep(0.5)
                self.find_element(BasePageLocators.PLACE_ORDER_BUTTON).click()
                self.wait_for_navigation(common_variables.restore_sleep_first_upsell_url, timeout=20000)
                break
            except:
                print(f'Populating CC number failed on the {attempt + 1} try! Retrying...')
        else:
            raise Exception(f'Entering CC number was not successful after {max_retries} retries!')

    def populate_cc_details(self):
        cc_exp_date = self.context.page.frame_locator(BasePageLocators.CC_EXP_DATE_FRAME).get_by_placeholder(BasePageLocators.CC_EXP_DATE_FIELD)
        cc_exp_date.press_sequentially(common_variables.test_cc_expiration_date)
        cc_cvv = self.context.page.frame_locator(BasePageLocators.CC_CVV_FRAME).get_by_placeholder(BasePageLocators.CC_CVV_FIELD)
        cc_cvv.press_sequentially(common_variables.test_cc_cvv)
        cc_zip = self.context.page.frame_locator(BasePageLocators.CC_ZIP_FRAME).get_by_placeholder(BasePageLocators.CC_ZIP_FIELD)
        cc_zip.press_sequentially(common_variables.test_cc_zip)
        time.sleep(1)
        self.retry_cc_number_entry()
        print('===> Populated CC details')
