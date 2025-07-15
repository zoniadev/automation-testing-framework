import common_variables
from pages.base_page_object import BasePage
from locators import *
from common_variables import *
from common_functions.parse_csv import parse_banner_mapping


class BlogPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)


    def open_blog_page(self):
        self.navigate_to_url(common_variables.zonia_blog_url)

    def select_blog_dropdown_category(self, dropdown, selection):
        dropdown_element = f"//a[@class='{dropdown} dropdown-toggle']"
        self.hover(dropdown_element)
        dropdown_category = f"//li[a[contains(text(), {selection})]]"
        self.click(dropdown_category)

    def verify_visible_banner_redirects(self):
        self.context.page.wait_for_load_state("load", timeout=BasePage.get_timeout(self))
        redirect_map = parse_banner_mapping()
        # Step 1: Capture the visible banner IDs
        visible_ids = self.context.page.eval_on_selector_all(
            '.blog-banner',
            '''nodes => nodes
                .filter(n => n.offsetParent !== null && !n.disabled)
                .map(n => n.getAttribute('data-id'))'''
        )
        if not visible_ids:
            print("⚠️ No visible banners found on page with class 'blog-banner'")
            return
        # Step 2: For each banner, immediately open the link in a new tab
        opened_pages = []
        for banner_id in visible_ids:
            print(f"🔍 Clicking banner: {banner_id}")
            if banner_id not in redirect_map:
                raise AssertionError(f"❌ Banner '{banner_id}' is visible but not found in redirect CSV")
            self.verify_element_visible(f'[data-id="{banner_id}"]')
            with self.context.page.context.expect_page() as new_page_info:
                self.context.page.locator(f'[data-id="{banner_id}"]').click()
            new_page = new_page_info.value
            opened_pages.append((banner_id, new_page))
        # Step 3: Now go through each opened page and verify its URL
        for banner_id, new_page in opened_pages:
            actual_url = new_page.url
            expected_url = redirect_map[banner_id]
            assert actual_url == expected_url, (
                f"❌ Redirect mismatch for {banner_id}:\nExpected: {expected_url}\nGot:      {actual_url}"
            )
            print(f"✅ Verified redirect: {banner_id} → {actual_url}")
            new_page.close()

    def check_this_week_articles(self):
        article_base_id = common_variables.blog_this_week_article
        for i in range(3):
            full_id = f'{article_base_id}-{i}'
            self.click(f'#{full_id}')
            self.context.page.wait_for_load_state("load", timeout=BasePage.get_timeout(self))
            self.verify_visible_banner_redirects()
