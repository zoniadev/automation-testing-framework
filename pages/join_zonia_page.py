import time
import common_variables
from pages.base_page_object import BasePage
from playwright.sync_api import expect
from locators import *


class JoinZoniaPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def join_zonia(self):
        print(f'>>> Joining Zonia...')
        if common_variables.funnel_prefix == 'pc':
            button_to_use = PATIENT_CARE_JOIN_BUTTON
            next_url = getattr(common_variables, f'{common_variables.funnel}_sign_up_url')
        else:
            button_to_use = JOIN_ZONIA_ID_BUTTON
            next_url = getattr(common_variables, f'{common_variables.funnel}_sign_up_url')
        self.context.page.locator(button_to_use).click()
        self.wait_for_navigation(next_url, timeout=20000)
        expect(self.context.page.locator(SIGNUP_NAME_FIELD)).to_be_visible()
        print(f'>>> Successfully joined Zonia')

    def join_zonia_screening(self, direct):
        print(f'>>> Joining Zonia on screening page...')
        if direct:
            self.context.page.locator(JOIN_ZONIA_ID_BUTTON).click()
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_sign_up_url'),
                                     timeout=20000)
        else:
            self.context.page.reload(wait_until="domcontentloaded")
            self.context.page.locator(JOIN_ZONIA_ID_BUTTON_TWL).click(timeout=30000)
            self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_join_zonia_url'), timeout=20000)
        print(f'>>> Successfully navigated to join Zonia from screening page')

    def join_zonia_replay_weekend(self):
        self.context.page.locator(JOIN_ZONIA_BUTTON).click()
        self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_rw_sales_url'), timeout=20000)
        self.context.page.locator(JOIN_ZONIA_ID_BUTTON).click()
        self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_rw_signup_url'), timeout=20000)
        print(f'>>> Successfully joined Zonia from replay weekend pages')

    def join_zonia_episode(self):
        self.context.page.locator(JOIN_ZONIA_ID_BUTTON).click()
        if common_variables.funnel == 'cr_bonus':
            next_page = getattr(common_variables, f'{common_variables.funnel}_rw_signup_url')
        elif common_variables.funnel == 'cr_live':
            next_page = getattr(common_variables, f'{common_variables.funnel}_sign_up_url')
        elif common_variables.funnel == 'cr_1ep':
            next_page = getattr(common_variables, f'{common_variables.funnel}_join_zonia_url')
        else:
            raise Exception(f'Unsupported parameter {common_variables.funnel}!')
        self.wait_for_navigation(next_page, timeout=20000)