import time
from pydoc import locate
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    __TIMEOUT = 15

    def __init__(self, browser):
        self.browser = browser
        self.browser_wait = WebDriverWait(browser, BasePage.__TIMEOUT)

    def verify_url(self, expected_url):
        current_url = self.browser.current_url
        assert expected_url == current_url, f"Expected {expected_url}, but got {current_url}"

    def wait_for_url_change(self, expected_url, timeout=__TIMEOUT):
        current_url = self.browser.current_url
        print('===> Waiting for URL change')
        try:
            WebDriverWait(self.browser, timeout).until(EC.url_changes(current_url))
            self.verify_url(expected_url)
            print(f"===> URL changed successfully to '{expected_url}'")
        except:
            actual_url = self.browser.current_url
            raise Exception(f"URL did not change within the specified time and is '{actual_url}'!")

    def find_single_element(self, locator, timeout=__TIMEOUT):
        element = locate(f'locators.{locator}')
        if element.startswith("//"):
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((By.XPATH, element)),
                message=f"Element with Xpath '{locator}' was not found!",
            )
        else:
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element)),
                message=f"Element with CSS '{locator}' was not found!",
            )

    def find_single_element_by_full_locator(self, locator, timeout=__TIMEOUT):
        """This method can be used from methods that construct dynamically the locator instead of using stored
                elements in locators.py """
        if locator.startswith("//"):
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator)),
                message=f"Element with Xpath '{locator}' was not found!",
            )
        else:
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)),
                message=f"Element with CSS '{locator}' was not found!",
            )

    def verify_element_visible(self, locator, timeout=__TIMEOUT):
        element = locate(f'locators.{locator}')
        web_driver_wait = WebDriverWait(self.browser, timeout)
        if element.startswith("//"):
            web_driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, element)),
                message=f"Element '{locator}' with Xpath {element} is not visible!",
            )
        else:
            web_driver_wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, element)),
                message=f"Element '{locator}' with CSS {element} is not visible!",
            )
        print(f"===> Verified element {locator} is present")

    def verify_element_visible_by_full_locator(self, locator, timeout=__TIMEOUT):
        """This method can be used from methods that construct dynamically the locator instead of using stored
        elements in locators.py """
        if locator.startswith("//"):
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)),
                                                       message=f"Element with Xpath {locator} is not visible!"),
        else:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)),
                                                       message=f"Element with CSS {locator} is not visible!"),

    def enter_text(self, text, locator):
        if text is None:
            raise Exception("Trying to populate field with None!")
        else:
            self.verify_element_visible(locator)
            print(f"===> Entering text: {text} in: {locator}")
            self.find_single_element(locator).send_keys(text)
            time.sleep(1)
            entered_text = self.find_single_element(locator).get_attribute("value")
            if locator not in ['signup_cc_number_field', 'signup_cc_expiration_field']:
                if entered_text != text:
                    raise Exception(f"{text} and {str(entered_text)} are not equal!")

    def click(self, locator):
        self.verify_element_visible(locator)
        print(f"===> Clicking element: {locator}")
        self.find_single_element(locator).click()

    def click_by_full_locator(self, locator):
        """This method can be used from methods that construct dynamically the locator instead of using stored
                elements in locators.py """
        self.verify_element_visible_by_full_locator(locator)
        print(f"===> Clicking element by full locator: {locator}")
        self.find_single_element_by_full_locator(locator).click()

    def get_text(self, locator):
        self.verify_element_visible(locator)
        for element_attr in ["text", "innerText", "value"]:
            text = self.find_single_element(locator).get_attribute(element_attr)
            if text and text != '':
                break
        return text

    def switch_to_iframe(self, locator):
        print(f'===> Switching to iframe "{locator}"')
        frame = self.find_single_element(locator)
        self.browser.switch_to.frame(frame)
        print(f'===> Inside iframe "{locator}"')

    def switch_to_default_content(self):
        self.browser.switch_to.default_content()

    def scroll_to_element(self, locator):
        element = self.find_single_element(locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        print(f'===> Scrolled to element "{locator}"')

    def verify_element_in_viewport(self, locator):
        element = self.find_single_element(locator)
        script = """
        var elem = arguments[0], box = elem.getBoundingClientRect();
        return box.top >= 0 && box.left >= 0 && 
               box.bottom <= (window.innerHeight || document.documentElement.clientHeight) && 
               box.right <= (window.innerWidth || document.documentElement.clientWidth);
        """
        element_visible = self.browser.execute_script(script, element)
        if element_visible:
            print(f'===> Verified element {locator} is visible in the displayed part of the page')
        else:
            raise Exception(f'Element {locator} is not visible in the displayed part of the page!')

