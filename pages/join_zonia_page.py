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
        self.context.page.locator(JOIN_ZONIA_ID_BUTTON).click()
        self.wait_for_navigation(getattr(common_variables, f'{common_variables.funnel}_sign_up_url'), timeout=20000)
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