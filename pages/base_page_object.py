import re
import time
from playwright.sync_api import Page, expect, Locator
import common_variables
from locators import *
import locators


class BasePage(object):
    __TIMEOUT = 30000
    _HIGHLIGHT_DELAY_MS = 2000

    def __init__(self, context):
        self.context = context

    def get_timeout(self):
        return BasePage.__TIMEOUT

    def find_element(self, locator):
        return self.context.page.locator(locator)

    def find_not_unique_element(self, locator, instance=1):
        timeout = self.get_timeout()
        poll_interval = 0.2  # seconds
        deadline = time.time() + (timeout / 1000)
        while time.time() < deadline:
            elements = self.context.page.locator(locator).all()
            visible_elements = [e for e in elements if e.is_visible()]
            if visible_elements:
                visible_elements_amount = len(visible_elements)
                if visible_elements_amount == 1:
                    print(f'===> One visible element with "{locator}" found from total {len(elements)}')
                    return visible_elements[0]
                elif visible_elements_amount > 1:
                    print(
                        f'===> {visible_elements_amount} visible elements with "{locator}" found from total {len(elements)}.')
                    if instance < visible_elements_amount:
                        return visible_elements[instance]
                    else:
                        print(f"===> Waiting for instance {instance} to appear...")
            else:
                print(f'===> No visible elements with "{locator}" yet...')
            time.sleep(poll_interval)
        raise Exception(
            f"Timeout exceeded: waited {timeout}ms for visible elements for locator '{locator}'."
        )

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
        self.highlight_element(element)
        element.click()
        print(f'===> Clicked element "{locator}"')

    def hover(self, locator):
        element = self.find_element(locator)
        element.scroll_into_view_if_needed()
        self.highlight_element(element)
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
        element = self.find_element(locator)
        element.scroll_into_view_if_needed()
        self.highlight_element(element)
        element.press_sequentially(text)
        print(f'===> Entered "{text}" in "{locator}" field')


    def verify_element_contain_text(self, locator, expected_text):
        expect(self.find_element(locator)).to_have_text(expected_text)


    def retry_cc_number_entry(self, max_retries=5, submit_button=PLACE_ORDER_BUTTON):
        cc_number = self.context.page.frame_locator(CC_NUM_FRAME).get_by_placeholder(CC_NUM_FIELD)
        cc_number.scroll_into_view_if_needed()
        self.highlight_element(cc_number)
        for attempt in range(max_retries):
            try:
                cc_number.fill("")
                cc_number.press_sequentially(common_variables.test_cc_number, delay=50)
                time.sleep(0.5)
                submit = self.find_element(submit_button)
                submit.scroll_into_view_if_needed()
                self.highlight_element(submit)
                submit.click()
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
        cc_exp_date.scroll_into_view_if_needed()
        self.highlight_element(cc_exp_date)
        cc_exp_date.press_sequentially(common_variables.test_cc_expiration_date)
        cc_cvv = self.context.page.frame_locator(CC_CVV_FRAME).get_by_placeholder(CC_CVV_FIELD)
        cc_cvv.scroll_into_view_if_needed()
        self.highlight_element(cc_cvv)
        if common_variables.test_cc_type == 'American Express':
            cc_cvv.press_sequentially('1111')
        else:
            cc_cvv.press_sequentially(common_variables.test_cc_cvv)
        cc_zip = self.context.page.frame_locator(CC_ZIP_FRAME).get_by_placeholder(CC_ZIP_FIELD)
        cc_zip.scroll_into_view_if_needed()
        self.highlight_element(cc_zip)
        cc_zip.press_sequentially(common_variables.test_cc_zip)
        cc_number = self.context.page.frame_locator(CC_NUM_FRAME).get_by_placeholder(CC_NUM_FIELD)
        cc_number.scroll_into_view_if_needed()
        self.highlight_element(cc_number)
        cc_number.fill("")
        cc_number.press_sequentially(common_variables.test_cc_number, delay=50)
        time.sleep(0.5)
        submit = self.find_element(submit_button)
        submit.scroll_into_view_if_needed()
        self.highlight_element(submit)
        submit.click()
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
                    self.highlight_element(button)
                    button.focus()
                    self.context.page.wait_for_timeout(500)
                    initial_position = button.bounding_box()
                    button.scroll_into_view_if_needed()
                    self.highlight_element(button)
                    button.click()
                    self.context.page.wait_for_timeout(500)
                    final_position = button.bounding_box()
                    if initial_position == final_position:
                        errors.append(f'Button {index} did not scroll down the page!')
                else:
                    # Handle button scrolling
                    target_element_locator = getattr(locators, target_element)
                    button.scroll_into_view_if_needed()
                    self.highlight_element(button)
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
                self.highlight_element(button)
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
        try:
            button = self.context.page.locator(ACCEPT_COOKIES_BUTTON)
            if button.count() > 0 and button.is_visible(timeout=1000):  # Short timeout
                print("Cookie banner detected. Attempting to accept...")
                try:
                    accept = self.find_element(ACCEPT_COOKIES_BUTTON)
                    accept.scroll_into_view_if_needed()
                    self.highlight_element(accept)
                    accept.click()
                    print("Cookie banner accepted.")
                except TimeoutError:
                    print("Accept button not found within the timeout.")
                except Exception as e:
                    print(f"An error occurred while handling the cookie banner: {e}")
            else:
                print("Cookie banner not detected.")
        except Exception as e:
            print(f"Error while checking cookie banner: {e}")

    def verify_placeholder_text(self, locator, expected_placeholder):
        element = self.find_element(locator)
        element.scroll_into_view_if_needed()
        self.highlight_element(element)
        actual_placeholder = element.get_attribute("placeholder")
        assert actual_placeholder == expected_placeholder, (
            f"Placeholder mismatch! Expected: '{expected_placeholder}', Actual: '{actual_placeholder}'"
        )

    def highlight_element(self, ctrl_locator: Locator, timeout_ms: int = None):
        if timeout_ms is None:
            timeout_ms = self._HIGHLIGHT_DELAY_MS
        if ctrl_locator.is_visible():
            ctrl_locator.evaluate("""(el) => {
                el.style.outline = '3px solid red'; // Temporary visual indicator
                el.style.transition = 'outline 0.5s ease';
            }""")
            time.sleep(timeout_ms / 1000)
            ctrl_locator.evaluate("""(el) => {
                el.style.outline = ''; // Clear the outline
            }""")
