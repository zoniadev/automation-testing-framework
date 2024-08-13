from behave import step
from pages import (
    SupplementStartPage,
    SupplementUpsellPage,
    WelcomePage,
    UserPage,
)


@step('user select to buy "{amount}" bottles in Restore Sleep Supplements page')
def user_fill_opt_in_form(context, amount):
    page = SupplementStartPage(context)
    page.buy_bottles(amount)


@step('user makes following decision in "{upsell_page}" Upsell page')
def user_select_in_upsell(context, upsell_page):
    page = SupplementUpsellPage(context)
    for row in context.table:
        page.chose_upsell(upgrade=row['upgrade'], last_chance=row['last_chance'])


@step('user makes following decision in 7 day free membership')
def user_select_seven_day_membership(context):
    page = SupplementUpsellPage(context)
    for row in context.table:
        page.chose_seven_day_membership(decision=row['decision'], plan=row['plan'])


@step('user complete registration')
def user_complete_registration(context):
    page = WelcomePage(context)
    page.create_password()
    page.skip_linking_social_media_accounts()
    page = UserPage(context)
    page.skip_questions()
    page.verify_registration()
