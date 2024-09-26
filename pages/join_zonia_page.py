import time
import common_variables
from pages.base_page_object import BasePage
from locators import *


class JoinZoniaPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def join_zonia(self):
        print(f'>>> Joining Zonia...')
        self.click(JOIN_ZONIA_ID_BUTTON, 0)
        self.wait_for_navigation(getattr(common_variables, f'{common_variables.series}_sign_up_url'), timeout=20000)
        time.sleep(1)
        self.verify_element_visible(SIGNUP_NAME_FIELD)
        print(f'>>> Successfully joined Zonia')