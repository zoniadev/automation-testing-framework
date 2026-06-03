from pages.base_page_object import BasePage

class DisclaimerPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def verify_disclaimer(self, url_entries):
        failed_pages = []
        total_urls = len(url_entries)
        for i, entry in enumerate(url_entries):
            url = entry["url"]
            expected_text = entry["disclaimer"]
            try:
                self.context.page.goto(url, wait_until="load", timeout=15000)
                # Check for the specific expected disclaimer text belonging to this exact URL
                if self.context.page.get_by_text(expected_text).count() == 0:
                    failed_pages.append({
                        "url": url,
                        "reason": f"Expected disclaimer text not found: '{expected_text}'"
                    })
                else:
                    print(f'Verified page <{i + 1} out of {total_urls}> "{url}"')
            except Exception as e:
                failed_pages.append({"url": url, "reason": str(e)})
        if failed_pages:
            error_details = "\n".join([f"- {item['url']}: {item['reason']}" for item in failed_pages])
            assert False, f"Verification failed for {len(failed_pages)} page(s):\n{error_details}"
        print("All pages validated successfully.")