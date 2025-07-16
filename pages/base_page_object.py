import re
import time
from playwright.sync_api import Page, expect
import common_variables
from locators import *
import locators


class BasePage(object):
    __TIMEOUT = 15000

    def __init__(self, context):
        self.context = context

    def find_element(self, locator):
        return self.context.page.locator(locator)

    def find_not_unique_element(self, locator, instance=1):
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
            return visible_elements[instance]

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

    def verify_element_visible(self, locator, timeout=__TIMEOUT):
        self.context.page.wait_for_selector(locator, timeout=timeout)
        expect(self.find_element(locator)).to_be_visible()
        print(f'===> Verified element "{locator}" is visible')

    def verify_element_not_visible(self, locator):
        elements = self.context.page.locator(locator).all()
        if elements:
            raise Exception(f'Element found with locator {locator}!')
        print(f'===> Verified element "{locator}" is not visible')

    def click(self, locator):
        element = self.find_element(locator)
        element.scroll_into_view_if_needed()
        element.click()
        print(f'===> Clicked element "{locator}"')

    def hover(self, locator):
        element = self.find_element(locator)
        element.hover()
        print(f'===> Hovered over element "{locator}"')

    def wait_for_navigation(self, url, timeout=__TIMEOUT):
        base_url = common_variables.used_base_url
        full_url_pattern = re.compile(f"^{re.escape(base_url)}{url}.*")
        print(f'===> Waiting for URL starting with "{base_url}{url}"')
        expect(self.context.page).to_have_url(full_url_pattern, timeout=timeout)
        print(f'===> URL successfully changed to "{base_url}{url}"')

    def get_text(self, locator):
        print(f'===> Getting text from element "{locator}"...')
        return self.find_element(locator).text_content()

    def enter_text(self, locator, text):
        self.find_element(locator).press_sequentially(text)
        print(f'===> Entered "{text}" in "{locator}" field')


    def verify_element_contain_text(self, locator, expected_text):
        expect(self.find_element(locator)).to_have_text(expected_text)


    def retry_cc_number_entry(self, max_retries=5, submit_button=PLACE_ORDER_BUTTON):
        cc_number = self.context.page.frame_locator(CC_NUM_FRAME).get_by_placeholder(CC_NUM_FIELD)
        for attempt in range(max_retries):
            try:
                cc_number.fill("")
                cc_number.press_sequentially(common_variables.test_cc_number, delay=50)
                time.sleep(0.5)
                self.find_element(submit_button).click()
                time.sleep(1)
                self.context.page.locator(LOADER).click()
                print('Loader found')
                break
            except Exception as E:
                print(f'Populating CC number failed on the {attempt + 1} try! Retrying...')
                print(f'Error: {E}')
        else:
            raise Exception(f'Entering CC number was not successful after {max_retries} retries!')

    def populate_cc_details(self, submit_button=PLACE_ORDER_BUTTON):
        cc_exp_date = self.context.page.frame_locator(CC_EXP_DATE_FRAME).get_by_placeholder(CC_EXP_DATE_FIELD)
        cc_exp_date.press_sequentially(common_variables.test_cc_expiration_date)
        cc_cvv = self.context.page.frame_locator(CC_CVV_FRAME).get_by_placeholder(CC_CVV_FIELD)
        if common_variables.test_cc_type == 'American Express':
            cc_cvv.press_sequentially('1111')
        else:
            cc_cvv.press_sequentially(common_variables.test_cc_cvv)
        cc_zip = self.context.page.frame_locator(CC_ZIP_FRAME).get_by_placeholder(CC_ZIP_FIELD)
        cc_zip.press_sequentially(common_variables.test_cc_zip)
        cc_number = self.context.page.frame_locator(CC_NUM_FRAME).get_by_placeholder(CC_NUM_FIELD)
        cc_number.fill("")
        cc_number.press_sequentially(common_variables.test_cc_number, delay=50)
        time.sleep(0.5)
        self.find_element(submit_button).click()
        expect(self.context.page.locator(LOADER)).not_to_be_visible(timeout=20000)
        print('===> Populated CC details')

    def navigate_to_url(self, url):
        base_url = common_variables.used_base_url
        full_url = base_url + url
        self.context.page.goto(full_url)

    def verify_all_buttons_links_on_a_page(self, element, expected_link):
        locator = getattr(locators, element)
        buttons = self.find_all_elements(locator)
        errors = []

        for index, button in enumerate(buttons, start=1):
            link = button.get_attribute("href")
            if link != expected_link:
                errors.append(f'Expected button {index} link to be "{expected_link}", but it is "{link}"!')

        if errors:
            error_count = len(errors)
            raise AssertionError(f"{error_count} errors found:\n" + "\n".join(errors))

    def verify_all_buttons_scroll(self, element, target_element):
        locator = getattr(locators, element)
        buttons = self.find_all_elements(locator)
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
                    target_element_locator = getattr(locators, target_element)
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
        full_expected_link = f'{common_variables.used_base_url}{expected_link}'
        buttons = self.find_all_elements(getattr(locators, element))
        errors = []

        for index, button in enumerate(buttons, start=1):
            if button.is_visible():
                button.scroll_into_view_if_needed()
                button.click()
                self.context.page.wait_for_load_state('load')
                new_url = self.context.page.url
                if full_expected_link != new_url:
                    errors.append(f'Expected button {index} to navigate to  "{full_expected_link}", but it went to "{new_url}"!')
                self.context.page.go_back()
        if errors:
            error_count = len(errors)
            raise AssertionError(f"{error_count} errors found:\n" + "\n".join(errors))

    def handle_cookie_banner(self):
        button = self.find_element(ACCEPT_COOKIES_BUTTON)
        if button.is_visible():
            print("Cookie banner detected. Attempting to accept...")
            try:
                self.click(ACCEPT_COOKIES_BUTTON)
                print("Cookie banner accepted.")
            except TimeoutError:
                print("Accept button not found within the timeout.")
            except Exception as e:
                print(f"An error occurred while handling the cookie banner: {e}")
        else:
            print("Cookie banner not detected.")

    def verify_placeholder_text(self, locator, expected_placeholder):
        element = self.find_element(locator)
        actual_placeholder = element.get_attribute("placeholder")
        assert actual_placeholder == expected_placeholder, (
            f"Placeholder mismatch! Expected: '{expected_placeholder}', Actual: '{actual_placeholder}'"
        )
