import time

import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *
import locators


class OptInPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def register_in_opt_in_page(self, form_to_use=None):
        if form_to_use:
            name_field = getattr(locators, f'{form_to_use}_ОPTIN_NAME_FIELD')
            email_field = getattr(locators, f'{form_to_use}_ОPTIN_EMAIL_FIELD')
            register_button = getattr(locators, f'{form_to_use}_REGISTER_BUTTON')
        else:
            name_field = OPTIN_NAME_FIELD
            email_field = OPTIN_EMAIL_FIELD
            register_button = REGISTER_BUTTON
        self.handle_cookie_banner()
        self.context.supplement_funnel_email = RD.automation_template_email()
        self.context.supplement_funnel_name = RD.automation_first_name()
        print(f'>>> Registering in Main Opt in page...')
        if form_to_use == 'POPUP':
            self.move_cursor_outside_viewport()
        if self.context.funnel == 'lg_live':
            self.enter_text(OPTIN_NAME_FIELD_AD_LIVE, self.context.supplement_funnel_name)
            self.enter_text(OPTIN_EMAIL_FIELD, self.context.supplement_funnel_email)
        elif self.context.mobile_run:
            self.enter_text(MOBILE_OPTIN_NAME_FIELD, self.context.supplement_funnel_name, method="type")
            self.enter_text(MOBILE_OPTIN_EMAIL_FIELD, self.context.supplement_funnel_email, method="type", delay=50)
        else:
            self.enter_text(name_field, self.context.supplement_funnel_name)
            self.enter_text(email_field, self.context.supplement_funnel_email)
        self.context.page.locator(register_button).click(timeout=30000)
        if self.context.funnel.startswith('bb_ev'):
            self.context.funnel = 'bb_ev'
        elif self.context.funnel.startswith('bb_live'):
            self.context.funnel = 'bb_live'
        elif self.context.funnel.startswith('ad_ev'):
            self.context.funnel = 'ad_ev'
        elif self.context.funnel.startswith('lg_ev'):
            self.context.funnel = 'lg_ev'
        elif self.context.funnel.startswith('lg_live'):
            self.context.funnel = 'lg_live'
        elif self.context.funnel.startswith('km_live'):
            self.context.funnel = 'km_live'
        elif self.context.funnel.startswith('is_ev'):
            self.context.funnel = 'is_ev'
        elif self.context.funnel.startswith('is_live'): # Added this condition
            self.context.funnel = 'is_live'             # Added this condition
        elif self.context.funnel.startswith('tf_ev'):
            self.context.funnel = 'tf_ev'
        elif self.context.funnel.startswith('km_ev'):
            self.context.funnel = 'km_ev'
        elif self.context.funnel.startswith('twl_evergreen'):
            self.context.funnel = 'twl_ev'
        elif self.context.funnel.startswith('cr_live'):
            self.context.funnel = 'cr_live'
        elif self.context.funnel.startswith('cr_ev'):
            self.context.funnel = 'cr_ev'
        elif self.context.funnel.startswith('cr_1ep'):
            self.context.funnel = 'cr_1ep'
        elif self.context.funnel.startswith('hh_live'):
            self.context.funnel = 'hh_live'
        elif self.context.funnel.startswith('hh_ev'):
            self.context.funnel = 'hh_ev'
        if self.context.funnel == 'twl_ev':
            self.wait_for_navigation(getattr(common_variables, f'{self.context.funnel}_screening_url'),
                                     timeout=20000)
        elif self.context.funnel == 'cr_1ep':
            self.wait_for_navigation(getattr(common_variables, f'{self.context.funnel}_ep1_live_url'),
                                     timeout=20000)
        else:
            attempted = []
            def try_nav(attr_name: str) -> bool:
                url_suffix = getattr(common_variables, attr_name, None)
                if not url_suffix:
                    raise AssertionError(f'{attr_name} is not defined in common_variables')
                attempted.append(f'{attr_name}="{url_suffix}"')
                try:
                    self.wait_for_navigation(url_suffix, timeout=20000)
                    return True
                except Exception as e:
                    print(f'>>> Navigation via {attr_name} failed: {e}')
                    return False
            rw_attr = f'{self.context.funnel}_rw_main_url'
            default_attr = f'{self.context.funnel}_join_zonia_url'

            if try_nav(default_attr):
                self.context.is_replay_weekend = False
                print('>>> Continuing with noramal flow!')
            elif try_nav(rw_attr):
                self.context.is_replay_weekend = True
                print('>>> Continuing with Replay Weekend flow!')
            else:
                raise AssertionError(
                    'Failed to navigate after opt-in. Tried: ' + (', '.join(attempted) or 'no configured URLs')
                )

    def register_in_episode_page(self, episode):
        self.context.page.locator(JOIN_ZONIA_ID_BUTTON).click()
        if episode in ['11', '12']:
            next_page = f'{self.context.docuseries_prefix}-join-zonia-bonuses-ep{episode}'
        else:
            next_page = getattr(common_variables, f'{self.context.funnel}_join_zonia_2_url')
        self.wait_for_navigation(next_page, timeout=20000)