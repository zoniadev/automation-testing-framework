from pages.base_page_object import BasePage

class DisclaimerPage(BasePage):
    def __init__(self, context):
        super().__init__(context)


    def verify_disclaimer(self, urls, expected_text):
        failed_pages = []
        total_urls = len(urls)
        for i, url in enumerate(urls):
            print(f"DEBUG: Navigating to URL: {url}")
            print(f"DEBUG: Searching for expected text: '{expected_text}'")
            try:
                self.context.page.goto(url, wait_until="load", timeout=15000)
                
                # Get all locators matching the text, visible or not
                all_locators = self.context.page.get_by_text(expected_text).all()
                print(f"DEBUG: Found {len(all_locators)} total disclaimers (visible or hidden) using get_by_text().")

                visible_locators = []
                for j, locator in enumerate(all_locators):
                    is_visible = locator.is_visible()
                    inner_text = locator.inner_text()
                    print(f"DEBUG: Total Match {j+1}: Visible={is_visible}, Text='{inner_text}'")
                    if is_visible:
                        visible_locators.append(locator)

                found_visible = len(visible_locators)
                print(f"DEBUG: Found {found_visible} *visible* disclaimers.")

                if found_visible > 0:
                    print(f"DEBUG: Disclaimer text '{expected_text}' was *visibly* found {found_visible} time(s).")
                    # Original logic: if disclaimer IS found, it's a failure
                    failed_pages.append({"url": url, "reason": f"Disclaimer text '{expected_text}' unexpectedly found {found_visible} time(s)."})
                else:
                    print(f'Verified page <{i + 1} out of {total_urls}> "{url}" - Disclaimer not found as expected.')
            except Exception as e:
                failed_pages.append({"url": url, "reason": str(e)})

        if failed_pages:
            error_details = "\n".join([f"- {item['url']}: {item['reason']}" for item in failed_pages])
            assert False, f"Verification failed for {len(failed_pages)} page(s):\n{error_details}"
        print("All pages validated successfully.")