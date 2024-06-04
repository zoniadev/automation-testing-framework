from random import shuffle

from faker import Faker

faker = Faker(["en_GB"])


def phone_number(min=100000000, max=999999999):
    number = str(faker.random_int(min, max))
    phone = "77" + number
    return phone


def random_number(min=10000000, max=99999999):
    number = str(faker.random_int(min, max))
    return number


def email():
    fake_email = faker.email()
    return fake_email


def email_with_added_digits(prefix: str, postfix: str) -> str:
    email_value = faker.email()
    email_arr = email_value.split("@")
    fake_email = prefix + "_" + email_arr[0] + "_" + random_number() + "@" + postfix
    return fake_email


def amount(min_amount=10000, max_amount=250000):
    loan_amount = str(faker.random_int(min_amount, max_amount))
    return loan_amount


def first_name():
    fake_first_name = faker.first_name()
    return fake_first_name


def middle_name():
    fake_middle_name = faker.first_name()
    return fake_middle_name


def last_name():
    fake_last_name = faker.last_name()
    return fake_last_name


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


def postcode():
    fake_postcode = faker.postcode()
    return fake_postcode


def random_sentence(nb_words=5):
    fake_sentence = faker.sentence(nb_words, variable_nb_words=True, ext_word_list=None)
    return fake_sentence


def random_company():
    fake_company = faker.company()
    return fake_company


def gmail_range() -> str:
    random_integer = list(random_number())
    random_string = list("abcdefgh")
    final_random_string = ""
    shuffle(random_integer)
    shuffle(random_string)
    edge_list = zip(random_integer, random_string)
    for a, b in edge_list:
        final_random_string += a
        final_random_string += b
    return final_random_string


def password(length=8):
    fake_password = faker.password(length)
    return fake_password