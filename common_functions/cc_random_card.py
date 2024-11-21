import random
import common_variables


def pick_payment_card():
    if common_variables.test_cc_type == 'random':
        selected_card = common_variables.test_cards[common_variables.card_index]
        common_variables.test_cc_number = selected_card["number"]
        common_variables.test_cc_type = selected_card["type"]
        common_variables.card_index = (common_variables.card_index + 1) % len(common_variables.test_cards)
    else:
        common_variables.test_cc_number = next(
            card["number"] for card in common_variables.test_cards if card["type"] == common_variables.test_cc_type
        )