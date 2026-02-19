import common_variables

def pick_payment_card(context):
    """
    Selects a credit card based on the type specified in context.
    
    Args:
        context: The Behave context object. Card details are stored in context.test_data.
    """
    card_type = context.test_data['cc_type']

    if card_type == 'random':
        selected_card = common_variables.test_cards[common_variables.card_index]
        cc_number = selected_card["number"]
        cc_type = selected_card["type"]
        common_variables.card_index = (common_variables.card_index + 1) % len(common_variables.test_cards)
    else:
        cc_number = next(
            card["number"] for card in common_variables.test_cards if card["type"] == card_type
        )
        cc_type = card_type

    # Store the result
    context.test_data['cc_number'] = cc_number
    context.test_data['cc_type'] = cc_type
