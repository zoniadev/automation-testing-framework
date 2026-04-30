import common_variables
from pages.base_page_object import BasePage
from locators import *


class UserPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def verify_registration(self):
        name_on_page = self.context.page.locator(USER_MENU_BUTTON).inner_text()
        assert self.context.supplement_funnel_name in name_on_page, (f'Expected name to be '
                                                                         f'"{self.context.supplement_funnel_name}",'
                                                                         f' but it is "{name_on_page}"!')
        print('===> Verified registration')
        print(f'Email: {self.context.supplement_funnel_email}')
        print(f'Pass: {self.context.supplement_funnel_password}')

    def navigate_to_video(self, video_title):
        # This is a placeholder for the hardcoded navigation logic.
        # You will need to replace the comments with actual Playwright commands
        # to navigate to the video pages.
        if video_title == "AAC - Understanding Your Aging Trajectory":
            self.navigate_to_url('user/aac-3/1')
        elif video_title == "AAC - The Ultimate Diet for Aging Gracefully":
            self.navigate_to_url('user/aac-3/4')
        else:
            self.search_for_series_and_episode(video_title)

    def search_for_series_and_episode(self, series_title):
        self.navigate_to_url(common_variables.search_results_page)
        self.context.page.locator(SEARCH_SHOWS_BUTTON).click()
        series, episode = series_title.split(" - ", 1)
        self.context.page.locator(SHOW_THUMBNAIL.format(value=series)).click()
        print(f'===> Opened series: {series_title}')
