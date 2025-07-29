import time

import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *


class OptInPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def register_in_opt_in_page(self):
        self.handle_cookie_banner()
        common_variables.supplement_funnel_email = RD.automation_template_email()
        common_variables.supplement_funnel_name = RD.automation_first_name()
        print(f'>>> Registering in Main Opt in page...')
        if common_variables.funnel == 'lg_live':
            self.enter_text(OPTIN_NAME_FIELD_AD_LIVE, common_variables.supplement_funnel_name)
        else:
            self.enter_text(OPTIN_NAME_FIELD, common_variables.supplement_funnel_name)
        self.enter_text(OPTIN_EMAIL_FIELD, common_variables.supplement_funnel_email)
        time.sleep(2)
        self.click(REGISTER_BUTTON)
        time.sleep(1)
        if common_variables.funnel.startswith('bb_ev'):
            common_variables.funnel = 'bb_ev'
        elif common_variables.funnel.startswith('bb_live'):
            common_variables.funnel = 'bb_live'
        elif common_variables.funnel.startswith('ad_ev'):
            common_variables.funnel = 'ad_ev'
        elif common_variables.funnel.startswith('lg_ev'):
            common_variables.funnel = 'lg_ev'
        elif common_variables.funnel.startswith('lg_live'):
            common_variables.funnel = 'lg_live'
        elif common_variables.funnel.startswith('km_live'):
            common_variables.funnel = 'km_live'
        elif common_variables.funnel.startswith('is_ev'):
            common_variables.funnel = 'is_ev'
        elif common_variables.funnel.startswith('tf_ev'):
            common_variables.funnel = 'tf_ev'
        elif common_variables.funnel.startswith('twl_evergreen'):
            common_variables.funnel = 'twl_ev'
        if common_variables.funnel == 'twl_ev':
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_screening_url'),
                                     timeout=20000)
        else:
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_join_zonia_url'), timeout=20000)
        self.verify_element_visible(JOIN_ZONIA_ID_BUTTON)
        print(f'>>> Successfully registered in Main Opt in page')