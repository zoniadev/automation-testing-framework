import re
import shutil
import threading
import datetime
import allure
from playwright.sync_api import sync_playwright
import common_variables
from common_functions import cc_random_card as CC
from common_functions.mongo_db import *

SCREENSHOTS_DIR = os.path.join(os.getcwd(), "screenshots")


def before_all(context):
    print(f"Starting run on {context.config.userdata['device'].capitalize()}")
    env = context.config.userdata.get("env")
    env_key = f"base_url_{env}"
    common_variables.used_base_url = getattr(common_variables, env_key)
    print(f"Starting run in {env.capitalize()} env")

    context.playwright = sync_playwright().start()

    allure_env_path = os.path.join("allure-results", "environment.properties")
    with open(allure_env_path, "w") as env_file:
        env_file.write(f"Device={context.config.userdata['device'].capitalize()}\n")
        env_file.write(f"Test_run_on={env.capitalize()}\n")


def before_feature(context, feature):
    print(f"Executing feature: '{context.feature.name}'")


def before_scenario(context, scenario):
    # Initialize mutable scenario state on context
    context.is_screening_flow = False
    context.is_replay_weekend = False
    context.flow_type = ''
    context.funnel = ''
    context.docuseries_prefix = ''
    context.bonus_episode = False
    context.membership_added = False
    context.docuseries_address_will_appear = False
    context.docuseries_address_already_filled = False
    context.mobile_run = False
    context.supplement_funnel_name = ''
    context.supplement_funnel_email = ''
    context.supplement_funnel_password = ''
    context.supplement_funnel_bottles = ''

    # Payment details on context
    context.test_cc_type = context.config.userdata['card_type']
    context.test_cc_number = ''
    context.test_cc_expiration_date = common_variables.test_cc_expiration_date
    context.test_cc_cvv = common_variables.test_cc_cvv
    context.test_cc_zip = common_variables.test_cc_zip
    context.card_index = common_variables.card_index
    context.test_cards = common_variables.test_cards

    CC.pick_payment_card(context)

    # Launch a fresh browser process per scenario to prevent state bleed between outline rows
    headless_str = context.config.userdata.get("headless")
    headless = headless_str.lower() == "true"
    browser_type = context.config.userdata.get("browser")

    if browser_type == "chrome":
        context.browser = context.playwright.chromium.launch(
            channel="chrome",
            headless=headless,
            slow_mo=200,
            args=["--autoplay-policy=no-user-gesture-required"]
        )
    else:
        context.browser = context.playwright.chromium.launch(
            headless=headless,
            slow_mo=200,
            args=["--autoplay-policy=no-user-gesture-required"]
        )

    if context.config.userdata['device'] == 'iphone':
        device = context.playwright.devices['iPhone 13']
    elif context.config.userdata['device'] == 'iphone_landscape':
        device = context.playwright.devices['iPhone 13 landscape']
    elif context.config.userdata['device'] == 'android':
        device = context.playwright.devices['Pixel 7']
    elif context.config.userdata['device'] == 'android_landscape':
        device = context.playwright.devices['Pixel 7 landscape']
    elif context.config.userdata['device'] == 'ipad':
        device = context.playwright.devices['iPad Pro 11']
    elif context.config.userdata['device'] == 'ipad_landscape':
        device = context.playwright.devices['iPad Pro 11 landscape']
    elif context.config.userdata['device'] == 'desktop':
        device = None
    else:
        raise Exception('Error setting device for execution! Possible parameters are "iphone", "iphone_landscape", "android", "android_landscape", "ipad" and "ipad_landscape"')

    record_video_str = context.config.userdata.get("record_video", "true")
    context.record_video = record_video_str.lower() == "true"

    context_args = {}
    if device:
        context_args.update(device)
        context.mobile_run = True
    else:
        # Build the Chrome version token from the actual launched browser
        # instead of a hardcoded one, so the UA never drifts out of sync
        # with the real engine again (it was previously stuck claiming
        # Chrome 91 from 2021 while running a much newer Chromium build -
        # a mismatch that can make sites/CDNs serve legacy code paths to an
        # engine that no longer has those quirks). "ZoniaTestingBrowser" is
        # kept verbatim in case anything downstream matches on it.
        context_args.update({
            "viewport": {'width': 1280, 'height': 720},
            "user_agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{context.browser.version} Safari/537.36 ZoniaTestingBrowser"
        })

    if context.record_video:
        context_args.update({
            "record_video_dir": f"screenshots/videos/{context.scenario.name}",
            "record_video_size": {"width": 640, "height": 480}
        })

    context.context = context.browser.new_context(**context_args)

    third_party_routes = [
        re.compile(r".*liflolrb\.marketise\.me/.*"),
        re.compile(r".*browser\.sentry-cdn\.com/.*"),
        re.compile(r".*js\.sentry-cdn\.com/.*"),
        re.compile(r".*stapecdn\.com/.*"),
        re.compile(r".*googletagmanager\.com/.*"),
    ]
    def _block_third_party(route):
        route.fulfill(status=204, body="")

    for blocked_route in third_party_routes:
        context.context.route(blocked_route, _block_third_party)

    context.page = context.context.new_page()

    # Track only the most recent top-level page navigation's HTTP status
    # (not every sub-resource - that was tried before and was mostly noise).
    # On failure this tells you at a glance whether the page itself was
    # actually served (e.g. a 503) instead of having to open a screenshot.
    context.last_page_status = None

    def _track_page_status(response):
        if response.request.is_navigation_request():
            context.last_page_status = f"{response.status} {response.url}"

    context.page.on("response", _track_page_status)


def before_step(context, step):
    context.step = step
    print(f"Executing step: {context.step.name}")


def after_step(context, step):
    if step.status == "failed":
        print(f"Failed step: {context.step.name}")
        print(f"Test failed on page: '{context.page.url}'")
        print("Taking screenshot")
        if not os.path.exists(SCREENSHOTS_DIR):
            os.makedirs(SCREENSHOTS_DIR)
        current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        scenario_name = context.scenario.name.replace(" ", "_")
        screenshot_filename = f"{scenario_name}_{current_time}.png"
        screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_filename)
        try:
            context.page.screenshot(
                path=screenshot_path,
                timeout=30000,
                animations="disabled",
                caret="hide"
            )
            print(f"Screenshot saved: {screenshot_path}")
            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
        except Exception as e:
            print(f"Error taking or attaching screenshot: {e}")
    else:
        print(f"Completed step: {context.step.name}")
    try:
        stdout = context.stdout_capture.getvalue()
        if stdout:
            allure.attach(stdout, name="stdout", attachment_type=allure.attachment_type.TEXT)
    except Exception:
        pass


def after_scenario(context, scenario):
    # Each teardown step is independently fault-tolerant: if the browser
    # already died mid-scenario (crash, OOM-kill, etc.), page.close() /
    # context.close() / browser.close() can all raise. Previously any one of
    # them raising would abort the rest of this hook, silently skipping the
    # "Failed scenario" print below - the scenario's outcome would then be
    # missing from test-summary.txt entirely instead of showing as failed.
    try:
        context.page.close()
    except Exception as e:
        print(f"Error closing page: {e}")

    try:
        context.context.close()
    except Exception as e:
        print(f"Error closing context: {e}")

    if context.record_video:
        video_dir = f"screenshots/videos/{context.scenario.name}"
        try:
            if os.path.exists(video_dir):
                video_files = os.listdir(video_dir)
                if scenario.status == "failed" and video_files:
                    video_path = os.path.join(video_dir, video_files[0])
                    if video_path.endswith(".webm"):
                        with open(video_path, "rb") as video:
                            allure.attach(video.read(), name="Test Video", attachment_type=allure.attachment_type.WEBM)
                shutil.rmtree(video_dir)
            else:
                allure.attach("Video recording was enabled, but no video file was found.", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            print(f"Error handling video for scenario: {e}")

    # Kill the browser process entirely — fresh process for the next outline row
    try:
        context.browser.close()
    except Exception as e:
        print(f"Error closing browser: {e}")

    if scenario.status == "failed":
        # Appended, never prepended - send-email.js colors this line by
        # checking line.startsWith('Failed scenario:'), so anything added
        # must come after the existing text, not before it.
        status_suffix = f"  [last page load: {context.last_page_status}]" if context.last_page_status else ""
        print(f"Failed scenario: '{context.scenario.name}'{status_suffix}")
    else:
        print(f"Completed scenario: '{context.scenario.name}'")


def after_feature(context, feature):
    if feature.status == "failed":
        print(f"Failed feature: '{context.feature.name}'")
    else:
        print(f"Completed feature: '{context.feature.name}'")


def _cleanup_automation_users_worker(result):
    try:
        client = connect_to_mongodb()
        delete_automation_users(client)
    except Exception as e:
        result["error"] = e


def after_all(context):
    print("Run completed")
    context.playwright.stop()
    print("Cleaning up the DB from old Automation users...")
    # The mongodb+srv:// DNS (SRV record) lookup isn't bounded by
    # serverSelectionTimeoutMS and can hang far longer than that on a
    # slow/blackholed network. Run it on a daemon thread with a hard
    # deadline so a stuck DNS lookup can't hang the whole test run.
    result = {}
    cleanup_thread = threading.Thread(
        target=_cleanup_automation_users_worker, args=(result,), daemon=True
    )
    cleanup_thread.start()
    cleanup_thread.join(timeout=15)
    if cleanup_thread.is_alive():
        print("!!! Automation users cleanup timed out after 15s (likely stuck DNS/network) — abandoning cleanup.")
    elif "error" in result:
        print(f"!!! Automation users cleanup failed: {result['error']}")