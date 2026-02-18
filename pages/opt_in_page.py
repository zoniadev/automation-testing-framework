import time

import common_functions.random_data as RD
import common_variables
from pages.base_page_object import BasePage
from locators import *


class OptInPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def register_in_opt_in_page(self):
        self.handle_cookie_banner()
        common_variables.supplement_funnel_email = RD.automation_template_email()
        common_variables.supplement_funnel_name = RD.automation_first_name()
        print(f'>>> Registering in Main Opt in page...')
        if common_variables.funnel == 'lg_live':
            self.context.page.locator(OPTIN_NAME_FIELD_AD_LIVE).fill(common_variables.supplement_funnel_name)
            self.context.page.locator(OPTIN_EMAIL_FIELD).fill(common_variables.supplement_funnel_email)
        elif common_variables.mobile_run:
            self.context.page.locator(MOBILE_OPTIN_NAME_FIELD).type(common_variables.supplement_funnel_name)
            self.context.page.locator(MOBILE_OPTIN_EMAIL_FIELD).type(common_variables.supplement_funnel_email, delay=50)
        else:
            self.context.page.locator(OPTIN_NAME_FIELD).fill(common_variables.supplement_funnel_name)
            self.context.page.locator(OPTIN_EMAIL_FIELD).fill(common_variables.supplement_funnel_email)
        self.context.page.locator(REGISTER_BUTTON).click(timeout=30000)
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
        elif common_variables.funnel.startswith('km_ev'):
            common_variables.funnel = 'km_ev'
        elif common_variables.funnel.startswith('twl_evergreen'):
            common_variables.funnel = 'twl_ev'
        elif common_variables.funnel.startswith('cr_live'):
            common_variables.funnel = 'cr_live'
        elif common_variables.funnel.startswith('cr_ev'):
            common_variables.funnel = 'cr_ev'
        elif common_variables.funnel.startswith('cr_1ep'):
            common_variables.funnel = 'cr_1ep'
        if common_variables.funnel == 'twl_ev':
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_screening_url'),
                                     timeout=20000)
        elif common_variables.funnel == 'cr_1ep':
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_ep1_live_url'),
                                     timeout=20000)
        else:
            attempted = []
            def try_nav(attr_name: str) -> bool:
                url_suffix = getattr(common_variables, attr_name, None)
                if not url_suffix:
                    return False
                attempted.append(f'{attr_name}="{url_suffix}"')
                try:
                    self.wait_for_navigation(url_suffix, timeout=20000)
                    return True
                except Exception as e:
                    print(f'>>> Navigation via {attr_name} failed: {e}')
                    return False
            rw_attr = f'{common_variables.funnel}_rw_main_url'
            default_attr = f'{common_variables.funnel}_join_zonia_url'

            if try_nav(default_attr):
                common_variables.is_replay_weekend = False
                print('>>> Continuing with noramal flow!')
            elif try_nav(rw_attr):
                common_variables.is_replay_weekend = True
                print('>>> Continuing with Replay Weekend flow!')
            else:
                raise AssertionError(
                    'Failed to navigate after opt-in. Tried: ' + (', '.join(attempted) or 'no configured URLs')
                )

    def register_in_episode_page(self, episode):
        self.context.page.locator(JOIN_ZONIA_ID_BUTTON).click()
        if episode in ['11', '12']:
            next_page = f'{common_variables.funnel_prefix}-join-zonia-bonuses-ep{episode}'
        else:
            next_page = getattr(common_variables, f'{common_variables.funnel}_join_zonia_2_url')
        self.wait_for_navigation(next_page, timeout=20000)
