import random
import common_variables


def pick_payment_card(context):
    if context.test_cc_type == 'random':
        selected_card = common_variables.test_cards[common_variables.card_index]
        context.test_cc_number = selected_card["number"]
        context.test_cc_type = selected_card["type"]
        common_variables.card_index = (common_variables.card_index + 1) % len(common_variables.test_cards)
    else:
        context.test_cc_number = next(
            card["number"] for card in common_variables.test_cards if card["type"] == context.test_cc_type
        )
