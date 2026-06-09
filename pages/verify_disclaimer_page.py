from pages.base_page_object import BasePage
import locators

SIGNUP_DISCLAIMERS = {
    "monthly": (
        'By clicking the "Activate My Membership" button below, a recurring monthly charge '
        'of $20 USD will automatically start today. You may cancel at any time. To cancel, '
        'go online to your Account and click on "Cancel Membership." If you cancel within the '
        'first 7 days you may request a full refund by emailing support@zonia.com. By proceeding, '
        'you agree to the Terms of Use and Privacy Policy.'
    ),
    "quarterly": (
        'By clicking the "Activate My Membership" button below, a recurring quarterly charge '
        'of $45 USD will automatically start today. You may cancel at any time. To cancel, '
        'go online to your Account and click on "Cancel Membership." If you cancel within the '
        'first 7 days you may request a full refund by emailing support@zonia.com. By proceeding, '
        'you agree to the Terms of Use and Privacy Policy.'
    ),
    "annually": (
        'By clicking the "Activate My Membership" button below, a recurring annual charge '
        'of $120 USD will automatically start today. You may cancel at any time. To cancel, '
        'go online to your Account and click on "Cancel Membership." If you cancel within the '
        'first 7 days you may request a full refund by emailing support@zonia.com. By proceeding, '
        'you agree to the Terms of Use and Privacy Policy.'
    ),
    "lifetime": (
        'By clicking "Activate My Membership," you agree to the Terms of Use and Privacy Policy. '
        'If you cancel within the first 7 days you may request a full refund by emailing support@zonia.com.'
    )
}


class DisclaimerPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def verify_disclaimer(self, url_entries):
        """Verifies static disclaimers for Opt-in pages based on CSV text."""
        failed_pages = []
        total_urls = len(url_entries)
        for i, entry in enumerate(url_entries):
            url = entry["url"]
            expected_text = entry["disclaimer"]
            try:
                self.context.page.goto(url, wait_until="load", timeout=15000)
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

    def verify_dynamic_disclaimers(self, url_entries):
        """Verifies dynamic disclaimers on Signup pages cycling through billing plans."""
        failed_pages = []
        total_urls = len(url_entries)
        standard_cycles = ["monthly", "quarterly", "annually"]
        for i, entry in enumerate(url_entries):
            url = entry["url"]
            try:
                self.context.page.goto(url, wait_until="load", timeout=15000)
                # 1. Verify standard cycles
                # OPTIMIZATION: Only handle cookie banner on the very first URL
                if i == 0:
                    self.handle_cookie_banner()
                for cycle in standard_cycles:
                    self.select_plan(cycle)
                    expected_text = SIGNUP_DISCLAIMERS[cycle]
                    if self.context.page.get_by_text(expected_text).count() == 0:
                        failed_pages.append({
                            "url": url,
                            "reason": f"Plan '{cycle}': Expected text not found."
                        })
                # 2. Conditional check for Lifetime plan
                lifetime_locator = getattr(locators, "LIFETIME_RADIO_BUTTON")
                if self.context.page.locator(lifetime_locator).is_visible():
                    self.select_plan("lifetime")
                    expected_text = SIGNUP_DISCLAIMERS["lifetime"]
                    if self.context.page.get_by_text(expected_text).count() == 0:
                        failed_pages.append({
                            "url": url,
                            "reason": "Plan 'lifetime': Expected text not found."
                        })
                else:
                    print(f'>>> Lifetime plan not present on "{url}" - skipping.')
                print(f'Verified signup page <{i + 1} out of {total_urls}> "{url}"')
            except Exception as e:
                failed_pages.append({"url": url, "reason": f"Execution error: {str(e)}"})
        if failed_pages:
            error_details = "\n".join([f"- {item['url']}: {item['reason']}" for item in failed_pages])
            assert False, f"Signup verification failed for {len(failed_pages)} page(s):\n{error_details}"
        print("All signup pages validated successfully.")

    def select_plan(self, cycle):
        """Selects the billing plan by clicking the corresponding radio button."""
        cycle_radiobutton = getattr(locators, f"{cycle.upper()}_RADIO_BUTTON")
        self.context.page.locator(cycle_radiobutton).click()
        print(f'>>> Selected {cycle} plan')