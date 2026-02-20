import re
import time
from playwright.sync_api import Page, expect
import common_variables
from common_functions.url_manager import URLManager


class BasePage(object):
    __TIMEOUT = 15000

    def __init__(self, context):
        self.context = context
        self.page = context.page
        
        # --- Locators ---
        self.place_order_button = self.page.locator("//button[@unique-id='order-btn-1']")
        
        # Frames
        self.cc_num_frame = self.page.frame_locator('//iframe[@id="braintree-hosted-field-number"]')
        self.cc_exp_frame = self.page.frame_locator('//iframe[@id="braintree-hosted-field-expirationDate"]')
        self.cc_cvv_frame = self.page.frame_locator('//iframe[@id="braintree-hosted-field-cvv"]')
        self.cc_zip_frame = self.page.frame_locator('//iframe[@id="braintree-hosted-field-postalCode"]')
        
        # Fields inside frames
        self.cc_number_input = self.cc_num_frame.get_by_placeholder('Card Number')
        self.cc_exp_date_input = self.cc_exp_frame.get_by_placeholder('Expiration Date(MM/YY)')
        self.cc_cvv_input = self.cc_cvv_frame.get_by_placeholder('Security Code(CCV)')
        self.cc_zip_input = self.cc_zip_frame.get_by_placeholder('Billing Zip/Postal Code')
        
        self.loader = self.page.locator("//*[@unique-id='loader-1']")
        self.join_zonia_button = self.page.locator("//a[text()='JOIN ZONIA NOW']")
        self.register_free_button = self.page.locator("//a[text()='Register for free now']")
        self.first_name_register_field = self.page.locator("//input[@id='first-name']")
        self.scroll_arrow_button = self.page.locator("//a[@class='arrow']")
        self.skip_survey_button = self.page.locator("*[unique-identifier='skip-survey-btn-1']")
        self.skip_health_track_button = self.page.locator('//*[@id="skip-health-track-btn"]')
        self.go_to_zonia_button = self.page.locator("*[unique-identifier='go-to-zonia-btn-1']")
        
        self.accept_cookies_button = self.page.locator("//button[@class='cookie-close-btn']")
        self.close_cookie_banner_button = self.page.locator("//button[@data-bs-dismiss='alert' and contains(@class, 'btn-close')]")
        
        self.chat_frame = self.page.locator('//iframe[@title="Chat"]')
        self.chat_close_button = self.page.locator('//*[@aria-label="Close widget"]')

    def get_timeout(self):
        return BasePage.__TIMEOUT

    def wait_for_navigation(self, url, timeout=__TIMEOUT):
        base_url = common_variables.used_base_url
        full_url_pattern = re.compile(f"^{re.escape(base_url)}{re.escape(url)}.*")
        print(f'===> Waiting for URL starting with "{base_url}{url}"')
        expect(self.page).to_have_url(full_url_pattern, timeout=timeout)
        print(f'===> URL successfully changed to "{self.page.url}"')
        
        if url == URLManager.get_url('welcome_page_url'):
            print('===> Performing additional check for "mode" parameter on welcome page.')
            expect(self.page).to_have_url(re.compile(r"(\?|&)mode="))
            print('===> "mode" parameter confirmed.')

    def verify_element_contain_text(self, locator, expected_text):
        element = locator if not isinstance(locator, str) else self.page.locator(locator)
        expect(element).to_have_text(expected_text)

    def retry_cc_number_entry(self, max_retries=5, submit_button=None):
        button_to_click = submit_button if submit_button else self.place_order_button
        
        self.cc_number_input.wait_for(state="visible", timeout=15000)
        test_cc_number = self.context.test_data['cc_number']
        
        for attempt in range(max_retries):
            print(f'Attempting CC number entry (Attempt {attempt + 1}/{max_retries})...')
            try:
                self.disable_chat()
                time.sleep(0.5)
                self.cc_number_input.fill("")
                time.sleep(0.5)
                self.cc_number_input.press_sequentially(test_cc_number, delay=50)
                
                self.page.wait_for_timeout(500)
                button_to_click.click()
                
                expect(self.cc_number_input).not_to_be_visible(timeout=20000)
                print('✅ CC number entry successful, navigating away from payment form.')
                return
            except Exception as E:
                if attempt == max_retries - 1:
                    raise Exception(f'Entering CC number failed after {max_retries} retries! Last Error: {E}')
                print(f'⚠️ Submission or number entry failed on attempt {attempt + 1}. Retrying...')
        raise Exception(f'Entering CC number was not successful after {max_retries} retries!')

    def populate_cc_details(self, submit_button=None):
        self.disable_chat()
        test_cc_type = self.context.test_data['cc_type']
        
        time.sleep(0.5)
        self.cc_exp_date_input.press_sequentially(common_variables.test_cc_expiration_date, delay=50)
        
        if test_cc_type == 'American Express':
            self.cc_cvv_input.fill('1111')
        else:
            self.cc_cvv_input.fill(common_variables.test_cc_cvv)
            
        self.cc_zip_input.fill(common_variables.test_cc_zip)
        self.retry_cc_number_entry(submit_button=submit_button)

    def navigate_to_url(self, url):
        base_url = common_variables.used_base_url
        full_url = base_url + url
        self.page.goto(full_url)
        print(f'===> Navigated to {full_url}')

    def verify_all_buttons_links_on_a_page(self, element_name, expected_link):
        # Legacy support: look up locator by name if passed as string
        if hasattr(self, element_name):
            locator = getattr(self, element_name)
            # If it's a property returning a Locator, use it. If string, wrap it.
            if isinstance(locator, str):
                buttons = self.page.locator(locator).all()
            else:
                buttons = locator.all()
        else:
             # Try to convert snake_case string to attribute name if needed (e.g. "PLACE_ORDER_BUTTON" -> "place_order_button")
             lower_name = element_name.lower()
             if hasattr(self, lower_name):
                 buttons = getattr(self, lower_name).all()
             else:
                 raise AttributeError(f"Locator '{element_name}' not found in {self.__class__.__name__}")

        errors = []
        for index, button in enumerate(buttons, start=1):
            link = button.get_attribute("href")
            if link != expected_link:
                errors.append(f'Expected button {index} link to be "{expected_link}", but it is "{link}"!')

        if errors:
            raise AssertionError(f"{len(errors)} errors found:\n" + "\n".join(errors))

    def verify_all_buttons_scroll(self, element_name, target_element_name):
        # Resolve source locator
        source = None
        if hasattr(self, element_name):
            source = getattr(self, element_name)
        elif hasattr(self, element_name.lower()):
            source = getattr(self, element_name.lower())
        else:
             raise AttributeError(f"Locator '{element_name}' not found")
             
        buttons = self.page.locator(source).all() if isinstance(source, str) else source.all()

        # Resolve target locator
        target_obj = None
        if target_element_name != "scroll_down":
            if hasattr(self, target_element_name):
                target = getattr(self, target_element_name)
            elif hasattr(self, target_element_name.lower()):
                target = getattr(self, target_element_name.lower())
            else:
                 raise AttributeError(f"Target '{target_element_name}' not found")
            
            target_obj = self.page.locator(target) if isinstance(target, str) else target

        errors = []
        for index, button in enumerate(buttons, start=1):
            try:
                if target_element_name == "scroll_down":
                    button.focus()
                    self.page.wait_for_timeout(500)
                    initial_position = button.bounding_box()
                    button.click()
                    self.page.wait_for_timeout(500)
                    final_position = button.bounding_box()
                    if initial_position == final_position:
                        errors.append(f'Button {index} did not scroll down the page!')
                else:
                    button.click()
                    target_obj.wait_for(state="visible", timeout=5000)
                    
                    box = target_obj.bounding_box()
                    if box:
                        viewport = self.page.viewport_size
                        is_in_viewport = (
                                box['y'] >= 0 and
                                box['x'] >= 0 and
                                (box['y'] + box['height']) <= viewport['height'] and
                                (box['x'] + box['width']) <= viewport['width']
                        )
                        if not is_in_viewport:
                            errors.append(f'Button {index} did not scroll to "{target_element_name}"!')
                    else:
                        errors.append(f'Button {index}: Bounding box not found for target')
            except Exception as e:
                errors.append(f'Button {index} error: {str(e)}')
        
        if errors:
            raise AssertionError(f"{len(errors)} errors found:\n" + "\n".join(errors))

    def verify_all_buttons_redirects_on_a_page(self, element_name, expected_link):
        full_expected_link = f'{common_variables.used_base_url}{expected_link}'
        
        source = None
        if hasattr(self, element_name):
            source = getattr(self, element_name)
        elif hasattr(self, element_name.lower()):
            source = getattr(self, element_name.lower())
        else:
             raise AttributeError(f"Locator '{element_name}' not found")
             
        buttons = self.page.locator(source).all() if isinstance(source, str) else source.all()

        errors = []
        for index, button in enumerate(buttons, start=1):
            if button.is_visible():
                button.scroll_into_view_if_needed()
                button.click()
                self.page.wait_for_load_state('load')
                new_url = self.page.url
                if full_expected_link != new_url:
                    errors.append(f'Expected button {index} to navigate to "{full_expected_link}", but it went to "{new_url}"!')
                self.page.go_back()
        if errors:
            raise AssertionError(f"{len(errors)} errors found:\n" + "\n".join(errors))

    def handle_cookie_banner(self, timeout=5000):
        possible_locators = [
            self.accept_cookies_button,
            self.close_cookie_banner_button
        ]
        for banner_locator in possible_locators:
            try:
                if banner_locator.is_visible(timeout=timeout):
                    banner_locator.click()
                    print(f"===> Cookie banner accepted.")
                    return
            except Exception:
                continue
        print("===> No cookie banner found.")

    def verify_placeholder_text(self, locator, expected_placeholder):
        element = locator if not isinstance(locator, str) else self.page.locator(locator)
        actual_placeholder = element.get_attribute("placeholder")
        assert actual_placeholder == expected_placeholder, (
            f"Placeholder mismatch! Expected: '{expected_placeholder}', Actual: '{actual_placeholder}'"
        )

    def disable_chat(self):
        self.page.evaluate("""() => {
            const el = document.querySelector("#fc_frame");
            if (el) el.remove();
        }""")

    def safe_fill(self, locator, value, timeout=30000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        self.disable_chat()
        
        field = locator if not isinstance(locator, str) else self.page.locator(locator)
        
        expect(field).to_be_attached(timeout=timeout)
        expect(field).to_be_visible(timeout=timeout)
        expect(field).to_be_editable(timeout=timeout)
        field.fill(value, timeout=timeout)
        expect(field).to_have_value(value, timeout=timeout)
