from random import shuffle
import time
from faker import Faker

faker = Faker(["en_US"])


def phone_number(min=100000000, max=999999999):
    number = str(faker.random_int(min, max))
    phone = "77" + number
    return phone
# def phone_number():
#     phone_number = faker.phone_number()
#     formatted_phone_number = faker.format("###-###-####", phone_number)
#     return formatted_phone_number

def random_number(min=10000000, max=99999999):
    number = str(faker.random_int(min, max))
    return number


def email():
    fake_email = faker.email()
    return fake_email

def epoch_date():
    return str(int(time.time()))


def automation_template_email():
    fake_email = "zoniat-v2" + last_name() + "-" + epoch_date() + "@gmail.com"
    return fake_email


def amount(min_amount=10000, max_amount=250000):
    loan_amount = str(faker.random_int(min_amount, max_amount))
    return loan_amount


def first_name():
    fake_first_name = faker.first_name()
    return fake_first_name

def automation_first_name():
    fake_first_name = 'Automation' + faker.first_name()
    return fake_first_name


def middle_name():
    fake_middle_name = faker.first_name()
    return fake_middle_name


def last_name(retries=5):
    for _ in range(retries):
        fake_last_name = faker.last_name()
        if len(fake_last_name) >= 3:
            return fake_last_name
    raise Exception(f"Could not generate a first name with minimum 3 characters after {retries} attempts!")


def full_name():
    full_name = f'{first_name()} {last_name()}'
    return full_name


def birthday(birthday_format):
    fake_birthday = faker.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=80)
    formatted_birthday = fake_birthday.strftime(birthday_format)
    return formatted_birthday


def address_line():
    fake_street = faker.street_name()
    fake_address_line = str(random_number(1, 999)) + " " + fake_street
    result = fake_address_line.replace("'", "")
    return result


def town():
    fake_town = faker.city()
    result = fake_town.replace("'", "")
    return result

def state():
    fake_town = faker.state()
    result = fake_town.replace("'", "")
    return result


def postcode():
    fake_postcode = faker.postcode()
    return fake_postcode


def random_sentence(nb_words=5):
    fake_sentence = faker.sentence(nb_words, variable_nb_words=True, ext_word_list=None)
    return fake_sentence


def random_company():
    fake_company = faker.company()
    return fake_company


def password(length=8):
    fake_password = faker.password(length)
    return fake_password
