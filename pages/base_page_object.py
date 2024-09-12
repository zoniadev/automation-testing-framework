import re
import time
from urllib.parse import urlparse
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
    LOADER = "//*[@test-id='loader']"
    JOIN_ZONIA_BUTTON = "//a[text()='JOIN ZONIA NOW']"
    REGISTER_FOR_FREE_NOW_BUTTON = "//a[text()='Register for free now']"
    FIRST_NAME_REGISTER_FIELD = "//input[@id='first-name']"
    SCROLL_ARROW_BUTTON = "//a[@class='arrow']"


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

    def find_all_elements(self, locator):
        elements = self.context.page.locator(locator).all()
        if not elements:
            raise Exception(f'No elements found with locator {locator}!')
        visible_elements = [element for element in elements if element.is_visible()]
        if not visible_elements:
            raise Exception(f'No visible elements found with locator {locator}!')
        visible_elements_amount = len(visible_elements)
        print(f'===> {visible_elements_amount} visible elements with "{locator}" found from total {len(elements)}.')
        return visible_elements

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
        expect(self.context.page).to_have_url(re.compile(f"^{url}.*"), timeout=timeout)
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
                self.context.page.locator(BasePageLocators.LOADER).click()
                print('Loader found')
                break
            except Exception as E:
                print(f'Populating CC number failed on the {attempt + 1} try! Retrying...')
                print(f'Error: {E}')
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
        expect(self.context.page.locator(BasePageLocators.LOADER)).not_to_be_visible(timeout=20000)
        print('===> Populated CC details')


    def navigate_to_url(self, url):
        self.context.page.goto(url)

    def verify_all_buttons_links_on_a_page(self, element, expected_link):
        buttons = self.find_all_elements(BasePageLocators.__dict__[element])
        errors = []

        for index, button in enumerate(buttons, start=1):
            link = button.get_attribute("href")
            if link != expected_link:
                errors.append(f'Expected button {index} link to be "{expected_link}", but it is "{link}"!')

        if errors:
            error_count = len(errors)
            raise AssertionError(f"{error_count} errors found:\n" + "\n".join(errors))

    def verify_all_buttons_scroll(self, element, target_element):
        buttons = self.find_all_elements(BasePageLocators.__dict__[element])
        errors = []
        for index, button in enumerate(buttons, start=1):
            try:
                if target_element == "scroll_down":
                    # Handle arrows scrolling
                    button.focus()
                    self.context.page.wait_for_timeout(500)
                    initial_position = button.bounding_box()
                    button.click()
                    self.context.page.wait_for_timeout(500)
                    final_position = button.bounding_box()
                    if initial_position == final_position:
                        errors.append(f'Button {index} did not scroll down the page!')
                else:
                    # Handle button scrolling
                    target_element_locator = BasePageLocators.__dict__[target_element]
                    button.click()
                    self.context.page.wait_for_selector(target_element_locator, timeout=5000)
                    # Get the target element handle
                    element_handle = self.context.page.query_selector(target_element_locator)
                    if element_handle:
                        # Get the bounding box of the target element
                        bounding_box = element_handle.bounding_box()
                        if bounding_box:
                            # Ensure all required keys are present
                            bounding_box = {key: bounding_box.get(key, 0) for key in ['top', 'left', 'bottom', 'right']}
                            # Check if the element is within the viewport (assuming viewport size of 1280x720)
                            viewport_width = 1280
                            viewport_height = 720
                            is_in_viewport = (
                                    bounding_box['top'] >= 0 and
                                    bounding_box['left'] >= 0 and
                                    bounding_box['bottom'] <= viewport_height and
                                    bounding_box['right'] <= viewport_width
                            )
                            if not is_in_viewport:
                                errors.append(f'Button {index} did not scroll to "{target_element}"!')
                        else:
                            errors.append(
                                f'Button {index}: The bounding box for the target element "{target_element}" could not be determined!')
                    else:
                        errors.append(
                            f'Button {index}: The target element "{target_element}" with locator "{target_element_locator}" was not found!')
            except Exception as e:
                errors.append(f'Button {index} encountered an error: {str(e)}')
        # Report errors if any
        if errors:
            error_count = len(errors)
            raise AssertionError(f"{error_count} errors found:\n" + "\n".join(errors))


    def verify_all_buttons_redirects_on_a_page(self, element, expected_link):
        buttons = self.find_all_elements(BasePageLocators.__dict__[element])
        errors = []

        for index, button in enumerate(buttons, start=1):
            button.click()
            self.context.page.wait_for_load_state('load')
            new_url = self.context.page.url
            if expected_link != new_url:
                errors.append(f'Expected button {index} to navigate to  "{expected_link}", but it went to "{new_url}"!')
            self.context.page.go_back()
        if errors:
            error_count = len(errors)
            raise AssertionError(f"{error_count} errors found:\n" + "\n".join(errors))
