import time

import common_functions.random_data as RD
from common_functions.url_manager import URLManager
from pages.base_page_object import BasePage
from locators import *


class OptInPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def register_in_opt_in_page(self):
        self.handle_cookie_banner()
        
        # Use context.test_data for email/name generation
        self.context.test_data['email'] = RD.automation_template_email()
        self.context.test_data['name'] = RD.automation_first_name()
        
        print(f'>>> Registering in Main Opt in page...')
        
        funnel = self.context.test_data['funnel']
        name = self.context.test_data['name']
        email = self.context.test_data['email']
        
        if funnel == 'lg_live':
            self.context.page.locator(OPTIN_NAME_FIELD_AD_LIVE).fill(name)
            self.context.page.locator(OPTIN_EMAIL_FIELD).fill(email)
        elif self.context.test_data.get('mobile_run'):
            self.context.page.locator(MOBILE_OPTIN_NAME_FIELD).type(name)
            self.context.page.locator(MOBILE_OPTIN_EMAIL_FIELD).type(email, delay=50)
        else:
            self.context.page.locator(OPTIN_NAME_FIELD).fill(name)
            self.context.page.locator(OPTIN_EMAIL_FIELD).fill(email)
            
        self.context.page.locator(REGISTER_BUTTON).click(timeout=30000)
        
        # Update funnel logic using context
        if funnel.startswith('bb_ev'):
            funnel = 'bb_ev'
        elif funnel.startswith('bb_live'):
            funnel = 'bb_live'
        elif funnel.startswith('ad_ev'):
            funnel = 'ad_ev'
        elif funnel.startswith('lg_ev'):
            funnel = 'lg_ev'
        elif funnel.startswith('lg_live'):
            funnel = 'lg_live'
        elif funnel.startswith('km_live'):
            funnel = 'km_live'
        elif funnel.startswith('is_ev'):
            funnel = 'is_ev'
        elif funnel.startswith('tf_ev'):
            funnel = 'tf_ev'
        elif funnel.startswith('km_ev'):
            funnel = 'km_ev'
        elif funnel.startswith('twl_evergreen'):
            funnel = 'twl_ev'
        elif funnel.startswith('cr_live'):
            funnel = 'cr_live'
        elif funnel.startswith('cr_ev'):
            funnel = 'cr_ev'
        elif funnel.startswith('cr_1ep'):
            funnel = 'cr_1ep'
            
        self.context.test_data['funnel'] = funnel
        
        if funnel == 'twl_ev':
            self.wait_for_navigation(URLManager.get_url(f'{funnel}_screening_url'), timeout=20000)
        elif funnel == 'cr_1ep':
            self.wait_for_navigation(URLManager.get_url(f'{funnel}_ep1_live_url'), timeout=20000)
        else:
            attempted = []
            def try_nav(attr_name: str) -> bool:
                try:
                    url_suffix = URLManager.get_url(attr_name)
                except AttributeError:
                    return False
                    
                attempted.append(f'{attr_name}="{url_suffix}"')
                try:
                    self.wait_for_navigation(url_suffix, timeout=20000)
                    return True
                except Exception as e:
                    print(f'>>> Navigation via {attr_name} failed: {e}')
                    return False
            
            rw_attr = f'{funnel}_rw_main_url'
            default_attr = f'{funnel}_join_zonia_url'

            if try_nav(default_attr):
                self.context.test_data['is_replay_weekend'] = False
                print('>>> Continuing with noramal flow!')
            elif try_nav(rw_attr):
                self.context.test_data['is_replay_weekend'] = True
                print('>>> Continuing with Replay Weekend flow!')
            else:
                raise AssertionError(
                    'Failed to navigate after opt-in. Tried: ' + (', '.join(attempted) or 'no configured URLs')
                )

    def register_in_episode_page(self, episode):
        self.context.page.locator(JOIN_ZONIA_ID_BUTTON).click()
        funnel = self.context.test_data['funnel']
        funnel_prefix = self.context.test_data['funnel_prefix']
        
        if episode in ['11', '12']:
            next_page = f'{funnel_prefix}-join-zonia-bonuses-ep{episode}'
        else:
            next_page = URLManager.get_url(f'{funnel}_join_zonia_2_url')

        self.wait_for_navigation(next_page, timeout=20000)
