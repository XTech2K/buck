import bid
import deck

from database import Database
from game import Game


def validated_input(game, player, prompt, function, *args):
    prompt = game.names[player] + prompt
    game.active_player = player
    db.update_game(game)
    result = None
    while result is None:
        result = function(input(prompt).lower(), *args)
    return result


db = Database(reset=True)
game = db.create_game()
print("Game ID: {}".format(game.game_id))

names = ['0', '1', '2', '3'] # TODO: player customizable names
game.names = names

while max(game.scores) < 52:
    game.reset_round()
    for i in range(4):
        print("{}'s hand: {}".format(game.names[i], game.hands[i]))

    for i in range(4):
        bidder = (game.dealer + 1 + i) % 4
        new_bid = validated_input(game, bidder, "'s bid: ", bid.validate_bid, game.winning_bid(), bidder == game.dealer)
        game.bids[bidder] = new_bid
        if new_bid != "pass":
            game.highest_bidder = bidder

    req_tricks = bid.value(game.bids[game.highest_bidder])
    trump = None

    if bid.modifier(game.winning_bid()) is None:
        game.leader = game.highest_bidder
        trump = validated_input(game, game.highest_bidder, " chooses trump: ", deck.validate_trump)
    else:
        game.leader = (game.highest_bidder - 1) % 4

    for trick in game.tricks:
        led = None
        for i in range(4):
            current_player = (game.leader + i) % 4
            print("Player {}'s hand: {}".format(current_player, game.hands[current_player]))
            print("Currently played cards: {}".format(trick))
            play = validated_input(game, current_player, " plays: ", deck.validate_play, game.hands[current_player], trump, led)
            card = game.hands[current_player].pop(play)
            if led is None:
                led = card[-1]
            trick[current_player] = card
        evals = [deck.eval_card(card, led, trump, bid.modifier(game.winning_bid())) for card in trick]
        winner = evals.index(max(evals))
        print("This trick is won by {} with {}!".format(game.names[winner], trick[winner]))
        game.taken[winner % 2] += 1
        game.leader = winner

    game.scores = bid.calculate_scores((game.highest_bidder + 1) % 2, game.taken, game.scores)
    print("Scores updated to {}".format(game.scores))
    game.dealer = (game.dealer + 1) % 4
