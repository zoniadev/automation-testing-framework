import time
import common_variables
import common_functions.random_data as RD
from features.lib.pages.base_page_object import BasePage


class RsFirstUpsellPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def chose_upsell(self, decision, upsell_page):
        upsell_url_navigation_map = {
            'first': common_variables.restore_sleep_second_upsell_url,
            'second': common_variables.restore_sleep_third_upsell_url,
            'third': common_variables.restore_sleep_fourth_upsell_url,
            'fourth': common_variables.welcome_page_url,
        }
        navigation_url = upsell_url_navigation_map.get(upsell_page)
        if navigation_url is None:
            raise Exception(f'Unsupported upsell page - "{upsell_page}"!')

        if decision == 'upgrade':
            button_decision = 'yes'
        elif decision == 'not upgrade':
            button_decision = 'no'
        else:
            raise Exception(f'Unsupported decision - "{decision}"!')
        self.scroll_to_element(f'first_upsell_{button_decision}_button')
        self.click(f'first_upsell_{button_decision}_button')
        self.wait_for_partial_url_change(navigation_url)
