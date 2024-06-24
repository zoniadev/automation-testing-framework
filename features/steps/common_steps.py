from behave import step
from common_functions import random_data as RD
from features.lib.pages import (
    JoinZoniaPage,
    OptInPage,
    SignUpPage,
    RestoreSleepPage,
    RsFirstUpsellPage,
)


@step('user fill opt-in form with name "{name}" and email "{email}"')
def user_fill_opt_in_form(context, name, email):
    page = OptInPage(context)
    page.register(name, email)


@step('user fill opt-in form with random name and email')
def user_fill_opt_in_form(context):
    page = OptInPage(context)
    page.register_random_user()



@step('user join Zonia')
def user_join_zonia(context):
    page = JoinZoniaPage(context)
    page.join()


@step('user sign-up with following data')
def user_sign_up(context):
    for row in context.table:
        page = SignUpPage(context)
        page.sign_up(bill_cycle=row['bill_cycle'], name=row['name'], email=row['email'], password=row['password'])


@step('user sign-up with random user data and bill cycle "{bill_cycle}"')
def user_sign_up(context, bill_cycle):
    page = SignUpPage(context)
    page.sign_up_with_random_data(bill_cycle)


@step('user verify Opt In register buttons')
def user_fill_opt_in_form(context):
    page = OptInPage(context)
    page.verify_register_buttons_navigation()


@step('user select to buy "{amount}" bottles in Restore Sleep Supplements page')
def user_fill_opt_in_form(context, amount):
    page = RestoreSleepPage(context)
    page.buy_bottles(amount)


@step('user select to "{decision}" in "{upsell_page}" Upsell page')
def user_fill_opt_in_form(context, decision, upsell_page):
    page = RsFirstUpsellPage(context)
    page.chose_upsell(decision, upsell_page)
