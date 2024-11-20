import random
import common_variables


def pick_payment_card():
    selected_card = common_variables.test_cards[common_variables.card_index]
    common_variables.test_cc_number = selected_card["number"]
    common_variables.test_cc_type = selected_card["type"]
    print(f'Scenario will use "{common_variables.test_cc_type}" card "{common_variables.test_cc_number}"')
    common_variables.card_index = (common_variables.card_index + 1) % len(common_variables.test_cards)