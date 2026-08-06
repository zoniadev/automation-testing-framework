from datetime import date, timedelta

from pages.base_page_object import BasePage
import locators


def _trial_disclaimer(plan_label, amount):
    """7-day-free-trial pages bill on a future date instead of "today"."""
    charge_date = date.today() + timedelta(days=7)
    return (
        f'By clicking the "Activate My Membership" button below, after your free 7-day free '
        f'membership, a recurring {plan_label} charge of ${amount} USD will automatically apply '
        f'and start on {charge_date.month}/{charge_date.day}/{charge_date.year}. You may cancel at '
        'any time. To cancel, go online to your Account and click on "Cancel Membership." If you '
        'cancel within the first 7 days you may request a full refund by emailing support@zonia.com. '
        'By proceeding, you agree to the Terms of Use and Privacy Policy.'
    )


# Keyed by the Signup.csv "type" column. Each entry maps plan name -> expected
# disclaimer text (static string) or a callable returning it (for text that
# depends on the current date). "one_time" pages have no plan selector at all,
# so they're handled separately via ONE_TIME_DISCLAIMER.
SIGNUP_DISCLAIMERS = {
    "standard": {
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
        ),
    },
    "trial": {
        "monthly": lambda: _trial_disclaimer("monthly", 20),
        "quarterly": lambda: _trial_disclaimer("quarterly", 45),
        "annually": lambda: _trial_disclaimer("annual", 120),
    },
}

ONE_TIME_DISCLAIMER = (
    'By clicking the "Place order securely" button below you agree to receive marketing emails '
    'from Zonia about products, events, and promotions. You may unsubscribe at any time. By '
    'proceeding with the registration, you agree to our Terms of Use and Privacy Policy.'
)


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
                self.context.page.goto(url, wait_until="domcontentloaded", timeout=15000)
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
        """Verifies disclaimers on Signup pages, per-URL behavior selected by its "type" column."""
        failed_pages = []
        total_urls = len(url_entries)
        standard_cycles = ["monthly", "quarterly", "annually"]
        for i, entry in enumerate(url_entries):
            url = entry["url"]
            page_type = entry.get("type", "standard")
            try:
                self.context.page.goto(url, wait_until="domcontentloaded", timeout=15000)
                # OPTIMIZATION: Only handle cookie banner on the very first URL
                if i == 0:
                    self.handle_cookie_banner()

                if page_type == "one_time":
                    if self.context.page.get_by_text(ONE_TIME_DISCLAIMER).count() == 0:
                        failed_pages.append({
                            "url": url,
                            "reason": "Expected one-time-purchase disclaimer not found."
                        })
                else:
                    templates = SIGNUP_DISCLAIMERS[page_type]
                    for cycle in standard_cycles:
                        self.select_plan(cycle)
                        expected_text = templates[cycle]() if callable(templates[cycle]) else templates[cycle]
                        if self.context.page.get_by_text(expected_text).count() == 0:
                            failed_pages.append({
                                "url": url,
                                "reason": f"Plan '{cycle}': Expected text not found."
                            })
                    # Conditional check for the Lifetime plan, where the template offers one
                    lifetime_locator = getattr(locators, "LIFETIME_RADIO_BUTTON")
                    if "lifetime" in templates and self.context.page.locator(lifetime_locator).is_visible():
                        self.select_plan("lifetime")
                        expected_text = templates["lifetime"]
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