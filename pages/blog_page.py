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
        redirect_map = parse_banner_mapping()
        # Step 1: Get all visible blog-banner elements and extract data-id attributes
        visible_ids = self.context.page.eval_on_selector_all(
            '.blog-banner',
            '''nodes => nodes
                .filter(n => n.offsetParent !== null && !n.disabled)
                .map(n => n.getAttribute('data-id'))'''
        )
        if not visible_ids:
            print("⚠️ No visible banners found on page with class 'blog-banner'")
            return
        for banner_id in visible_ids:
            print(f"🔍 Checking banner: {banner_id}")
            if banner_id not in redirect_map:
                raise AssertionError(f"❌ Banner '{banner_id}' is visible but not found in redirect CSV")
            expected_url = redirect_map[banner_id]
            locator = self.find_element(f'[data-id="{banner_id}"]')
            try:
                locator.wait_for(state="visible", timeout=1000)
                with self.context.page.context.expect_page() as new_page_info:
                    locator.click()
                new_page = new_page_info.value
                new_page.wait_for_load_state("load", timeout=10000)
                actual_url = new_page.url
                assert actual_url == expected_url, (
                    f"❌ Redirect mismatch for {banner_id}:\nExpected: {expected_url}\nGot:      {actual_url}"
                )
                print(f"✅ Verified redirect: {banner_id} → {actual_url}")
                new_page.close()
            except Exception as e:
                raise AssertionError(f"⚠️ Verification failed for {banner_id}: {e}")
