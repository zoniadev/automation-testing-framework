# from behave import step
from common_functions.custom_step_decorator import step
import common_variables
from common_functions.url_manager import URLManager
import common_functions.random_data as RD
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
    print(f'Scenario will use "{context.test_data["cc_type"]}" card "{context.test_data["cc_number"]}"')
    context.test_data['flow_type'] = 'supplement'
    context.test_data['funnel'] = funnel.lower().replace(' ', '_')
    
    page = SupplementStartPage(context)
    page.navigate_to_url(URLManager.get_url(f"{context.test_data['funnel']}_start_url"))
    page.supplement_funnel_buy_bottles(amount, funnel)
    context.test_data['bottles'] = amount


@step('user makes following decision in "{order}" supplement "{upsell_page}" Upsell page')
def user_select_in_supplement_upsell(context, order, upsell_page):
    page = SupplementUpsellPage(context)
    if context.test_data.get('bottles') != '1':
        page.change_order_delay_timeout(30)
    for row in context.table:
        page.chose_supplement_upsell(order, upsell_page, upgrade=row['upgrade'], last_chance=row['last_chance'])


@step('user makes following decision in docuseries "{upsell_page}" Upsell page')
def user_select_in_docuseries_upsell(context, upsell_page):
    page = SupplementUpsellPage(context)
    if upsell_page == 'Booster Packages':
        if context.test_data['bonus_episode'] or context.test_data['is_replay_weekend']:
            reason = "bonus episode" if context.test_data['bonus_episode'] else "replay weekend"
            print(f"===> Skipping Booster Packages upsell because this flow is for {reason}")
            return
        else:
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
        if row['decision'] == 'accept' and row['plan'] != 'no':
            context.test_data['membership_added'] = True
        else:
            context.test_data['membership_added'] = False


@step('user complete registration')
def user_complete_registration(context):
    page = WelcomePage(context)
    if context.test_data['flow_type'] == 'supplement':
        page.create_password()
        if context.test_data['membership_added']:
            page.skip_survey()
    if context.test_data['flow_type'] == 'docuseries':
        page.skip_survey()
    page = UserPage(context)
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
    print(f'Scenario will use "{context.test_data["cc_type"]}" card "{context.test_data["cc_number"]}"')
    context.test_data['flow_type'] = 'docuseries'
    context.test_data['funnel'] = series.lower()
    context.test_data['funnel_prefix'] = context.test_data['funnel'].split('_')[0]
    
    page = OptInPage(context)
    page.navigate_to_url(URLManager.get_url(f"{series.lower()}_opt_in_url"))
    page.register_in_opt_in_page()


@step(u'user join Zonia')
def user_join_zonia(context):
    page = JoinZoniaPage(context)
    if context.test_data['is_replay_weekend']:
        page.join_zonia_replay_weekend()
    elif context.test_data['is_screening_flow']:
        page.join_zonia_episode()
    else:
        page.join_zonia()


@step(u'user join Zonia in 1 episode page')
def user_join_zonia_1ep(context):
    page = JoinZoniaPage(context)
    page.join_zonia_episode()


@step(u'user join Zonia in screening page "{route}"')
def user_join_zonia_in_screening(context, route):
    direct = ''
    if route == 'directly':
        direct = True
    else:
        direct = False
    page = JoinZoniaPage(context)
    page.join_zonia_screening(direct)


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


@step(u'user is on the Patient Care sales page')
def user_open_patient_care_page(context):
    context.test_data['flow_type'] = 'docuseries'
    context.test_data['funnel'] = 'pc'
    context.test_data['funnel_prefix'] = 'pc'
    context.test_data['email'] = RD.automation_template_email()
    context.test_data['name'] = RD.automation_first_name()
    
    page = JoinZoniaPage(context)
    page.handle_cookie_banner()
    page.navigate_to_url(URLManager.get_url("pc_sales_page_url"))


@step(u'user is on the "{series}" episode "{episode}" page')
def user_is_on_episode_page(context, series, episode):
    context.test_data['flow_type'] = 'docuseries'
    if episode in ['11', '12']:
        context.test_data['bonus_episode'] = True
    else:
        context.test_data['is_screening_flow'] = True
        
    context.test_data['funnel'] = series.lower()
    context.test_data['funnel_prefix'] = context.test_data['funnel'].split('_')[0]
    
    if episode in ['11', '12']:
        page_url = f'{context.test_data["funnel_prefix"]}_bonus_episode_{episode}_url'
    else:
        page_url = f'{context.test_data["funnel_prefix"]}_episode_{episode}_url'
        
    context.test_data['email'] = RD.automation_template_email()
    context.test_data['name'] = RD.automation_first_name()
    
    page = OptInPage(context)
    page.navigate_to_url(URLManager.get_url(page_url))
    page.register_in_episode_page(episode)
