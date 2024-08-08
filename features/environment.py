import datetime
import os

from playwright.sync_api import sync_playwright
import common_variables


def before_all(context):
    print("Starting run")
    common_variables.funnel = context.config.userdata["funnel"]
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)


def before_feature(context, feature):
    print(f"Executing feature: '{context.feature.name}'")


def before_scenario(context, scenario):
    start_page = context.config.userdata.get("start_page")
    url_to_use = getattr(common_variables, start_page)
    context.context = context.browser.new_context(
        viewport={'width': 1280, 'height': 720},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    context.page = context.context.new_page()
    context.page.goto(url_to_use)


def before_step(context, step):
    context.step = step
    print(f"Executing step: {context.step.name}")


def after_step(context, step):
    if step.status == "failed":
        print(f"Failed step: {context.step.name}")
        print("Taking screenshots")
    else:
        print(f"Completed step: {context.step.name}")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        print(f"Failed scenario: '{context.scenario.name}'")
        screenshot_path = os.path.join('screenshots', f"{scenario.name}.png")
        context.page.screenshot(path=screenshot_path)
        print(f"Saved screenshot: '{scenario.name}.png'")
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
