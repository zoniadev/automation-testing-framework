from behave import step
from common_functions import random_data as RD
from features.lib.pages import (
    JoinZoniaPage,
    OptInPage,
    SignUpPage,
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


@step('user sign-up with random data')
def user_sinn_with_random_data(context):
    page = SignUpPage(context)
    page.sign_up('monthly', name=RD.first_name(), email=RD.email(), password=RD.password())


@step('user verify Opt In register buttons')
def user_fill_opt_in_form(context):
    page = OptInPage(context)
    page.verify_register_buttons_navigation()

