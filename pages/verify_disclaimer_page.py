from pages.base_page_object import BasePage

class DisclaimerPage(BasePage):
    def __init__(self, context):
        super().__init__(context)


    def verify_disclaimer(self, urls, expected_text):
        failed_pages = []
        total_urls = len(urls)
        for i, url in enumerate(urls):
            try:
                self.context.page.goto(url, wait_until="load", timeout=15000)
                if self.context.page.get_by_text(expected_text).count() == 0:
                    failed_pages.append({"url": url, "reason": "Disclaimer text not found."})
                else:
                    print(f'Verified page <{i + 1} out of {total_urls}> "{url}"')
            except Exception as e:
                failed_pages.append({"url": url, "reason": str(e)})

        if failed_pages:
            error_details = "\n".join([f"- {item['url']}: {item['reason']}" for item in failed_pages])
            assert False, f"Verification failed for {len(failed_pages)} page(s):\n{error_details}"
        print("All pages validated successfully.")