BIDS = ['pass', '3', '4', '5', '6', '12', '24', '48']
MODIFIERS = ['l', 'h']


class Bid:
    def __init__(self, bid , modifier=None):
        self.value = bid
        self.modifier = modifier


def value(bid):
    return int(bid[:-1] if bid[-1] in MODIFIERS else bid)

def modifier(bid):
    return bid[-1] if bid[-1] in MODIFIERS else None

def parse_bid(bid):
    return Bid(bid[:-1], bid[-1]) if bid[-1] in MODIFIERS else Bid(bid, None)

def update_scores(game):
    bid_value = value(game.winning_bid())
    bidding = game.highest_bidder % 2
    non_bidding = (bidding + 1) % 2
    game.scores[bidding] += bid_value if game.taken[bidding] >= min(bid_value, 6) else -max(bid_value, 6)
    game.scores[non_bidding] += game.taken[non_bidding] if game.taken[non_bidding] > 0 else -max(bid_value, 6)

def validate_bid(bid_str, prev_str, is_dealer):
    if len(bid_str) == 0:
        print("Must enter a bid!")
        return None

    bid = parse_bid(bid_str)
    prev = parse_bid(prev_str) if prev_str is not None else Bid("pass")

    if bid.value not in BIDS or bid.value == "pass" and bid.modifier is not None:
        print("Invalid bid of {}!".format(bid_str))
    elif bid.value == "pass":
        if prev.value == "pass":
            print("Cannot pass the first bid!")
        else:
            return bid_str
    elif bid.modifier is not None and bid.value not in BIDS[1:5]:
        print("Bid of {} cannot have a modifier!".format(bid.value))
    elif BIDS.index(bid.value) <= BIDS.index(prev.value) if prev.modifier is None else BIDS.index(prev.bid) - 1:
        print("Bid of {} is too low to beat existing bid of {}!".format(bid_str, prev_str))
    elif bid.value == "48" and not (prev.value == "24" and is_dealer):
        print("Cannot Hossenfeffer unless last bid was 24 and you are dealer!")
    else:
        return bid_str
    return None
