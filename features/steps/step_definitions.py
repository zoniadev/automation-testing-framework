# from behave import step
from common_functions.custom_step_decorator import step
import common_variables
from pages import (
    SupplementStartPage,
    SupplementUpsellPage,
    WelcomePage,
    UserPage,
    OptInPage,
    JoinZoniaPage,
    SignUpPage,
    BlogPage,
    BasePage,
)


@step('user select to buy "{amount}" bottles in "{funnel}" Supplements page')
def user_fill_opt_in_form(context, amount, funnel):
    print(f'Scenario will use "{common_variables.test_cc_type}" card "{common_variables.test_cc_number}"')
    common_variables.funnel = funnel.lower().replace(' ', '_')
    page = SupplementStartPage(context)
    page.navigate_to_url(getattr(common_variables, f"{common_variables.funnel}_start_url"))
    page.supplement_funnel_buy_bottles(amount, funnel)
    common_variables.supplement_funnel_bottles = amount


@step('user makes following decision in "{order}" supplement "{upsell_page}" Upsell page')
def user_select_in_supplement_upsell(context, order, upsell_page):
    page = SupplementUpsellPage(context)
    if common_variables.supplement_funnel_bottles != '1':
        page.change_order_delay_timeout(30)
    for row in context.table:
        page.chose_supplement_upsell(order, upsell_page, upgrade=row['upgrade'], last_chance=row['last_chance'])


@step('user makes following decision in docuseries "{upsell_page}" Upsell page')
def user_select_in_docuseries_upsell(context, upsell_page):
    page = SupplementUpsellPage(context)
    if upsell_page == 'Booster Packages':
        for row in context.table:
            page.chose_docuseries_booster_package_upsell(decision=row['decision'])
    elif upsell_page == 'Masterclass Packages':
        for row in context.table:
            page.chose_docuseries_masterclass_upsell(decision=row['decision'])
    elif upsell_page in ['Restore Detox', 'Restore Life', 'Restore Sleep']:
        for row in context.table:
            page.docuseries_buy_upsells(upsell_page, amount=row['bottles'], upsell_downsell=row['upsell_downsell'])


@step('user makes following decision in 7 day free membership')
def user_select_seven_day_membership(context):
    page = SupplementUpsellPage(context)
    for row in context.table:
        page.chose_seven_day_membership(decision=row['decision'], plan=row['plan'])
    common_variables.membership_added = True


@step('user complete registration')
def user_complete_registration(context):
    page = WelcomePage(context)
    if common_variables.membership_added:
        page.create_password()
    page.skip_linking_social_media_accounts()
    page = UserPage(context)
    page.skip_questions()
    page.verify_registration()


@step(u'Verify "{element}" links on "{url}" page are "{link}"')
def verify_button_links(context, element, url, link):
    page = BasePage(context)
    page.navigate_to_url(url)
    page.verify_all_buttons_links_on_a_page(element, link)


@step(u'Verify "{element}" scrolling to "{target_element}" on "{url}" page')
def verify_all_buttons_scroll(context, element, target_element, url):
    page = BasePage(context)
    page.navigate_to_url(url)
    page.verify_all_buttons_scroll(element, target_element)


@step(u'Verify "{element}" button/s on "{url}" page navigate to "{expected_redirect}"')
def verify_button_redirects(context, element, url, expected_redirect):
    page = BasePage(context)
    page.navigate_to_url(url)
    page.verify_all_buttons_redirects_on_a_page(element, expected_redirect)


@step(u'user register in "{series}" Opt In page')
def user_register_in_opt_in_page(context, series):
    print(f'Scenario will use "{common_variables.test_cc_type}" card "{common_variables.test_cc_number}"')
    common_variables.funnel = series.lower()
    common_variables.funnel_prefix = common_variables.funnel.split('_')[0]
    page = OptInPage(context)
    page.navigate_to_url(getattr(common_variables, f"{series.lower()}_opt_in_url"))
    page.register_in_opt_in_page()


@step(u'user join Zonia')
def user_join_zonia(context):
    page = JoinZoniaPage(context)
    page.join_zonia()

@step(u'user join Zonia in screening page')
def user_join_zonia_in_screening(context):
    page = JoinZoniaPage(context)
    page.join_zonia_screening()


@step(u'user sign up for "{cycle}" plan')
def user_sign_up_for_cycle_plan(context, cycle):
    page = SignUpPage(context)
    page.select_plan(cycle.upper())
    page.register_in_signup_page(cycle)


@step(u'Verify banners redirects in "{dropdown}" and "{dropdown_category}"')
def verify_banners_in_category(context, dropdown, dropdown_category):
    page = BlogPage(context)
    page.open_blog_page()
    page.select_blog_dropdown_category(dropdown, dropdown_category)
    page.verify_visible_banner_redirects()


@step(u'Verify banners redirects in this week articles')
def verify_banners_in_this_week_articles(context):
    page = BlogPage(context)
    page.open_blog_page()
    page.check_this_week_articles()
