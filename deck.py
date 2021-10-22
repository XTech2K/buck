from random import shuffle

SUITS = ['d', 'h', 'c', 's']
EXTENDED_SUITS = ['diamonds', 'hearts', 'clubs', 'spades']
REDS = ['d', 'h']
VALUES = ['9', 't', 'j', 'q', 'k', 'a']

deck = [v + s for s in SUITS for v in VALUES]


def deal():
    shuffle(deck)
    hands = [[], [], [], []]
    for i in range(8):
        hands[i % 4].extend(deck[i * 3: i * 3 + 3])
    return hands


def eval_card(card, trump, led, rule):
    value, suit = VALUES.index(card[0]) + 1, card[1]
    if rule is None and value == 3 and (suit in REDS) == (trump in REDS):
        return 14 if suit == trump else 13
    elif rule is None and suit == trump:
        return value + 6
    elif suit == led:
        return value if rule != 'l' else value * -1 + 7
    else:
        return 0


def validate_trump(trump):
    if trump in SUITS:
        return trump
    elif trump in EXTENDED_SUITS:
        return SUITS[EXTENDED_SUITS.index(trump)]
    else:
        print("{} is an invalid trump!".format(trump))
        return None


def validate_play(play, hand, led):
    if not play.isnumeric():
        print("Please pick a card index to play!")
        return None
    else:
        play = int(play)
    if play < 0 or play >= len(hand):
        print("You don't have a card at index {}!")
    elif hand[play][-1] != led:
        other_options = [card[-1] == led for card in hand]
        if sum(other_options) > 0:
            print("You could have played along with the led suit!")
        else:
            return play
    else:
        return play
    return None
