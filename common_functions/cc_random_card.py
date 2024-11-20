import random
import common_variables


def pick_payment_card():
    remaining_cards = common_variables.test_cards.copy()
    if not remaining_cards:
        common_variables.used_cards = []
        remaining_cards = common_variables.test_cards.copy()

    selected_card = random.choice(remaining_cards)
    remaining_cards.remove(selected_card)
    common_variables.used_cards.append(selected_card)

    common_variables.test_cc_number = selected_card["number"]
    common_variables.test_cc_type = selected_card["type"]
    print(f'Scenario will use "{common_variables.test_cc_type}" card "{common_variables.test_cc_number}"')