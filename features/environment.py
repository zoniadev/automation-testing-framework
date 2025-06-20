import datetime
import os
import shutil
import allure
from playwright.sync_api import sync_playwright
import common_variables
from common_functions import cc_random_card as CC
from common_functions.mongo_db import *

SCREENSHOTS_DIR = os.path.join(os.getcwd(), "screenshots")


def before_all(context):
    print(f"Starting run on {context.config.userdata['device'].capitalize()}")
    context.playwright = sync_playwright().start()
    headless_str = context.config.userdata.get("headless")
    headless = headless_str.lower() == "true"
    context.browser = context.playwright.chromium.launch(headless=headless, slow_mo=200)

    allure_env_path = os.path.join("allure-results", "environment.properties")
    with open(allure_env_path, "w") as env_file:
        env_file.write(f"device={context.config.userdata['device'].capitalize()}\n")

    env = context.config.userdata.get("env")
    env_key = f"base_url_{env}"
    common_variables.used_base_url = getattr(common_variables, env_key)


def before_feature(context, feature):
    print(f"Executing feature: '{context.feature.name}'")


def before_scenario(context, scenario):
    common_variables.test_cc_type = context.config.userdata['card_type']
    CC.pick_payment_card()
    context.console_messages = []
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
        raise Exception('Error setting device for execution! Possible parameters are "iphone", "iphone_landscape", '
                        '"android", "android_landscape", "ipad" and "ipad_landscape"')
    if device:
        context.context = context.browser.new_context(**device,
                                                      record_video_dir=f"screenshots/videos/{context.scenario.name}",
                                                      record_video_size={"width": 640, "height": 480}
                                                      )
    else:
        context.context = context.browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            record_video_dir=f"screenshots/videos/{context.scenario.name}",
            record_video_size={"width": 640, "height": 480}
        )
    context.page = context.context.new_page()

    def handle_console_message(msg):
        context.console_messages.append({
            'type': msg.type,
            'text': msg.text
        })
    context.page.on("console", handle_console_message)


def before_step(context, step):
    context.step = step
    print(f"Executing step: {context.step.name}")


def after_step(context, step):
    if step.status == "failed":
        print(f"Failed step: {context.step.name}")
        print(f"Test failed on page: '{context.page.url}'")
        print("Taking screenshots")
        if not os.path.exists(SCREENSHOTS_DIR):
            os.makedirs(SCREENSHOTS_DIR)
        current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        scenario_name = context.scenario.name.replace(" ", "_")
        screenshot_filename = f"{scenario_name}_{current_time}.png"
        screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_filename)
        context.page.screenshot(path=screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        # Filter the captured console messages for errors
        console_errors = [msg['text'] for msg in context.console_messages if msg['type'] == 'error']
        if console_errors:
            print("Captured the following browser console errors:")
            for error in console_errors:
                print(f'--- {error}')
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
    video_dir = f"screenshots/videos/{context.scenario.name}"
    context.page.close()
    context.context.close()
    if os.path.exists(video_dir):
        if scenario.status == "failed":
            video_path = os.path.join(video_dir, os.listdir(video_dir)[0])
            if video_path.endswith(".webm"):
                with open(video_path, "rb") as video:
                    allure.attach(video.read(), name="Test Video", attachment_type=allure.attachment_type.WEBM)
        try:
            shutil.rmtree(video_dir)
        except Exception as e:
            print(f"Error deleting video directory: {e}")
    else:
        allure.attach("No video recording found for this scenario.", attachment_type=allure.attachment_type.TEXT)
    if scenario.status == "failed":
        print(f"Failed scenario: '{context.scenario.name}'")
    else:
        print(f"Completed scenario: '{context.scenario.name}'")
    common_variables.docuseries_address_will_appear = False
    common_variables.docuseries_address_already_filled = False


def after_feature(context, feature):
    if feature.status == "failed":
        print(f"Failed feature: '{context.feature.name}'")
    else:
        print(f"Completed feature: '{context.feature.name}'")


def after_all(context):
    print("Run completed")
    context.browser.close()
    context.playwright.stop()
    print("Cleaning up the DB from old Automation users...")
    try:
        client = connect_to_mongodb()
        delete_automation_users(client)
    except Exception as e:
        print(f"!!! Automation users cleanup failed: {e}")
