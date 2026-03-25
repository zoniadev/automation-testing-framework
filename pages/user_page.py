import common_variables
from pages.base_page_object import BasePage
from locators import *


class UserPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def verify_registration(self):
        name_on_page = self.context.page.locator(USER_MENU_BUTTON).inner_text()
        assert common_variables.supplement_funnel_name in name_on_page, (f'Expected name to be '
                                                                         f'"{common_variables.supplement_funnel_name}",'
                                                                         f' but it is "{name_on_page}"!')
        print('===> Verified registration')
        print(f'Email: {common_variables.supplement_funnel_email}')
        print(f'Pass: {common_variables.supplement_funnel_password}')

    def navigate_to_video(self, video_title):
        # This is a placeholder for the hardcoded navigation logic.
        # You will need to replace the comments with actual Playwright commands
        # to navigate to the video pages.
        if video_title == "First Hardcoded Video Title":
            self.navigate_to_url('user/aac-3/1')
        elif video_title == "Second Hardcoded Video Title":
            self.navigate_to_url('user/aac-3/4')
        elif video_title == "Third Hardcoded Video Title":
            self.navigate_to_url('user/aac-3/4')
        else:
            raise ValueError(f"Navigation logic for video '{video_title}' is not defined.")
