from behave import step
from pages import (
    RestoreSleepPage,
    RsFirstUpsellPage,
)


@step('user select to buy "{amount}" bottles in Restore Sleep Supplements page')
def user_fill_opt_in_form(context, amount):
    page = RestoreSleepPage(context)
    page.buy_bottles(amount)


@step('user makes following decision in "{upsell_page}" Upsell page')
def user_select_in_upsell(context, upsell_page):
    page = RsFirstUpsellPage(context)
    for row in context.table:
        page.chose_upsell(upgrade=row['upgrade'], last_chance=row['last_chance'])
