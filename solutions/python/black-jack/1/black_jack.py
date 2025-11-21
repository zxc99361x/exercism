def value_of_card(card):
    if card=='K' or card=='Q' or card=='J':
        return 10
    elif card=='A':
        return 1
    else:
        return int(card)
def higher_card(card_one, card_two):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 1
        else:
            return int(card)
    value_one = card_value(card_one)
    value_two = card_value(card_two)
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two
def value_of_ace(card_one, card_two):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 1
        else:
            return int(card)
    value_one = card_value(card_one)
    value_two = card_value(card_two)
    if card_one == 'A' or card_two == 'A':
        return 1
    if value_one+value_two<21 and value_one+value_two>10:
        return 1
    if value_one+value_two<=10:
        return 11
def is_blackjack(card_one, card_two):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
    value_one = card_value(card_one)
    value_two = card_value(card_two)
    if value_one+value_two==21:
        return True
    else :
        return False
def can_split_pairs(card_one, card_two):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
    value_one = card_value(card_one)
    value_two = card_value(card_two)
    if value_one==value_two:
        return True
    else:
        return False
def can_double_down(card_one, card_two):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 1
        else:
            return int(card)

    total = card_value(card_one) + card_value(card_two)

    if total in [9, 10, 11]:
        return True
    else:
        return False
