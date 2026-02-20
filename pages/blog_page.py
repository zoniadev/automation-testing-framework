import common_variables
from common_functions.url_manager import URLManager
from pages.base_page_object import BasePage
from common_functions.parse_csv import parse_banner_mapping


class BlogPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def open_blog_page(self):
        self.navigate_to_url(URLManager.get_url('zonia_blog_url'))

    def select_blog_dropdown_category(self, dropdown, selection):
        # Dynamic locators based on arguments
        dropdown_element = self.page.locator(f"//a[@class='{dropdown} dropdown-toggle']")
        dropdown_element.hover()
        
        dropdown_category = self.page.locator(f"//li[a[contains(text(), {selection})]]")
        dropdown_category.click()

    def verify_visible_banner_redirects(self):
        self.page.wait_for_load_state("load", timeout=BasePage.get_timeout(self))
        redirect_map = parse_banner_mapping()
        # Step 1: Capture the visible banner IDs
        visible_ids = self.page.eval_on_selector_all(
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
            
            banner_locator = self.page.locator(f'[data-id="{banner_id}"]')
            
            if not banner_locator.is_visible():
                raise AssertionError(f"❌ Banner '{banner_id}' is not visible")
            with self.context.context.expect_page() as new_page_info:
                banner_locator.click()
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
        article_base_id = URLManager.get_url('blog_this_week_article')
        for i in range(3):
            full_id = f'{article_base_id}-{i}'
            self.page.locator(f'#{full_id}').click()
            self.verify_visible_banner_redirects()
