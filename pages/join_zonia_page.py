import time
from common_functions.url_manager import URLManager
from pages.base_page_object import BasePage
from playwright.sync_api import expect


class JoinZoniaPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        
        # --- Locators ---
        self.join_zonia_id_button = self.page.locator("*[unique-id='register-btn-1']")
        self.join_zonia_id_button_twl = self.page.locator("*[unique-id='register-btn-3']")
        self.patient_care_join_button = self.page.locator("*[data-testid='join-zonia-today-desktop']")
        self.signup_name_field = self.page.locator("input[id='form-name']") # Needed for verification
        self.join_zonia_button = self.page.locator("a:text('JOIN ZONIA NOW')")

    def join_zonia(self):
        print(f'>>> Joining Zonia...')
        
        funnel_prefix = self.context.test_data['funnel_prefix']
        funnel = self.context.test_data['funnel']
        
        if funnel_prefix == 'pc':
            button_to_use = self.patient_care_join_button
            next_url = URLManager.get_url(f'{funnel}_sign_up_url')
        else:
            button_to_use = self.join_zonia_id_button
            next_url = URLManager.get_url(f'{funnel}_sign_up_url')
            
        button_to_use.click()
        self.wait_for_navigation(next_url, timeout=20000)
        expect(self.signup_name_field).to_be_visible()
        print(f'>>> Successfully joined Zonia')

    def join_zonia_screening(self, direct):
        print(f'>>> Joining Zonia on screening page...')
        funnel = self.context.test_data['funnel']
        
        if direct:
            self.join_zonia_id_button.click()
            self.wait_for_navigation(URLManager.get_url(f'{funnel}_sign_up_url'), timeout=20000)
        else:
            self.page.reload(wait_until="domcontentloaded")
            self.join_zonia_id_button_twl.click(timeout=30000)
            self.wait_for_navigation(URLManager.get_url(f'{funnel}_join_zonia_url'), timeout=20000)
        print(f'>>> Successfully navigated to join Zonia from screening page')

    def join_zonia_replay_weekend(self):
        funnel = self.context.test_data['funnel']
        
        self.join_zonia_button.click()
        self.wait_for_navigation(URLManager.get_url(f'{funnel}_rw_sales_url'), timeout=20000)
        self.join_zonia_id_button.click()
        self.wait_for_navigation(URLManager.get_url(f'{funnel}_rw_signup_url'), timeout=20000)
        print(f'>>> Successfully joined Zonia from replay weekend pages')

    def join_zonia_episode(self):
        funnel = self.context.test_data['funnel']
        
        self.join_zonia_id_button.click()
        if funnel == 'cr_bonus':
            next_page = URLManager.get_url(f'{funnel}_rw_signup_url')
        elif funnel == 'cr_live':
            next_page = URLManager.get_url(f'{funnel}_sign_up_url')
        elif funnel == 'cr_1ep':
            next_page = URLManager.get_url(f'{funnel}_join_zonia_url')
        else:
            raise Exception(f'Unsupported parameter {funnel}!')
        self.wait_for_navigation(next_page, timeout=20000)
