import datetime
import os
import allure
from playwright.sync_api import sync_playwright
import common_variables

SCREENSHOTS_DIR = os.path.join(os.getcwd(), "screenshots")


def before_all(context):
    print("Starting run")
    context.playwright = sync_playwright().start()
    headless_str = context.config.userdata.get("headless")
    headless = headless_str.lower() == "true"
    context.browser = context.playwright.chromium.launch(headless=headless, slow_mo=200)


def before_feature(context, feature):
    print(f"Executing feature: '{context.feature.name}'")


def before_scenario(context, scenario):
    context.console_messages = []
    context.context = context.browser.new_context(
        viewport={'width': 1280, 'height': 720},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    context.page = context.context.new_page()

    # Listen to console events and capture errors
    def handle_console_message(msg):
        # Append all messages to the list with type and text
        context.console_messages.append({
            'type': msg.type,
            'text': msg.text
        })
    # Attach the listener to the page
    context.page.on("console", handle_console_message)


def before_step(context, step):
    context.step = step
    print(f"Executing step: {context.step.name}")


def after_step(context, step):
    if step.status == "failed":
        print(f"Failed step: {context.step.name}")
        # Filter the captured console messages for errors
        console_errors = [msg['text'] for msg in context.console_messages if msg['type'] == 'error']
        if console_errors:
            print("Captured the following browser console errors:")
            for error in console_errors:
                print(f'--- {error}')
        print("Taking screenshots")
        allure.attach(
            context.page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    else:
        print(f"Completed step: {context.step.name}")
    try:
        stdout = context.stdout_capture.getvalue()
        if stdout:
            allure.attach(stdout, name="stdout", attachment_type=allure.attachment_type.TEXT)
    except Exception:
        pass


def after_scenario(context, scenario):
    if scenario.status == "failed":
        print(f"Failed scenario: '{context.scenario.name}'")
        if not os.path.exists(SCREENSHOTS_DIR):
            os.makedirs(SCREENSHOTS_DIR)
        current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        scenario_name = scenario.name.replace(" ", "_")
        screenshot_filename = f"{scenario_name}_{current_time}.png"
        screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_filename)
        context.page.screenshot(path=screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        print(f"Test failed on page: '{context.page.url}'")
    else:
        print(f"Completed scenario: '{context.scenario.name}'")
    context.page.close()
    context.context.close()


def after_feature(context, feature):
    if feature.status == "failed":
        print(f"Failed feature: '{context.feature.name}'")
    else:
        print(f"Completed feature: '{context.feature.name}'")


def after_all(context):
    print("Run completed")
    context.browser.close()
    context.playwright.stop()
