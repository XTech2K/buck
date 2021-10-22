import bid
import deck
from game import Game
from player import Player


def validated_input(prompt, function, *args):
    result = None
    while result is None:
        result = function(input(prompt).lower(), *args)
    return result


players = [Player() for i in range(4)]
game = Game(players)

while max(game.scores) < 52:
    hands = deck.deal()
    for i in range(4):
        players[i].hand = hands[i]
        print("Player {}'s hand: {}".format(i, players[i].hand))

    current_bid = bid.Bid("pass", None)
    final_bidder = 0
    bidder = game.dealer
    for i in range(4):
        bidder = (bidder + 1) % 4
        new_bid = validated_input("Player {}'s bid: ".format(bidder), bid.validate_bid, current_bid, bidder == game.dealer)
        if new_bid.value != "pass":
            current_bid = new_bid
            final_bidder = bidder

    req_tricks = current_bid.required_value()
    trump = None

    if current_bid.modifier is None:
        leader = final_bidder
        trump = validated_input("Player {} chooses trump: ".format(final_bidder), deck.validate_trump)
    else:
        leader = (game.dealer + 1) % 4

    tricks = [0, 0]
    for i in range(6):
        in_play = [None] * 4
        led = None
        for j in range(4):
            current_player = (leader + j) % 4
            print("Player {}'s hand: {}".format(current_player, hands[current_player]))
            print("Currently played cards: {}".format(in_play))
            play = validated_input("Player {} plays: ".format(current_player), deck.validate_play, players[current_player].hand, led)
            card = players[current_player].hand.pop(play)
            if led is None:
                led = card[-1]
            in_play[current_player] = card
        evals = [deck.eval_card(card, led, trump, current_bid.modifier) for card in in_play]
        winner = evals.index(max(evals))
        print("This trick is won by {} with {}!".format(winner, in_play[winner]))
        tricks[winner % 2] += 1
        leader = winner
    game.scores = current_bid.calculate_scores((final_bidder + 1) % 2, tricks, game.scores)
    print("Scores updated to {}".format(game.scores))
    game.dealer = (game.dealer + 1) % 4
