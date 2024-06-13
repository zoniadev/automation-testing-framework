import datetime
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import common_variables


def before_all(context):
    print("Starting run")


def before_feature(context, feature):
    print(f"Executing feature: '{context.feature.name}'")


def before_scenario(context, scenario):
    service = Service()
    options = webdriver.ChromeOptions()
    if context.config.userdata.get("headless"):
        options.add_argument("--headless")
        print('===> Running in Headless mode')
    # Get URL from behave parameters
    start_page = context.config.userdata.get("start_page")
    url_to_use = getattr(common_variables, start_page)
    print(f"Executing scenario: '{context.scenario.name}'")
    context.browser = webdriver.Chrome(service=service, options=options)
    context.browser.get(url_to_use)


def before_step(context, step):
    context.step = step
    print(f"Executing step: {context.step.name}")


def after_step(context, step):
    if step.status == "failed":
        print(f"Failed step: {context.step.name}")
        print("Taking screenshots")
        dtm = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        context.browser.save_screenshot("screenshots/%s-%s.png" % (context.scenario.name, dtm))
        allure.attach(
            context.browser.get_screenshot_as_png(),
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
    else:
        print(f"Completed scenario: '{context.scenario.name}'")
    context.browser.quit()


def after_feature(context, feature):
    if feature.status == "failed":
        print(f"Failed feature: '{context.feature.name}'")
    else:
        print(f"Completed feature: '{context.feature.name}'")


def after_all(context):
    print("Run completed")
