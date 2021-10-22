BIDS = ['pass', '3', '4', '5', '6', '12', '24', '48']
MODIFIERS = ['l', 'h']


class Bid:
    def __init__(self, bid, modifier):
        self.value = bid
        self.modifier = modifier

    def with_mod(self):
        return self.value + self.modifier if self.modifier is not None else self.value

    def required_value(self):
        return int(self.value)

    def calculate_scores(self, bidding_team, tricks, scores):
        non_bidding_team = (bidding_team + 1) % 2
        if self.value in BIDS[-4:]:
            if tricks[bidding_team] == 6:
                scores[bidding_team] += self.value
                scores[non_bidding_team] -= self.value
            else:
                scores[bidding_team] -= self.value
                scores[non_bidding_team] += tricks[non_bidding_team]
        else:
            if tricks[bidding_team] >= self.value:
                scores[bidding_team] += self.value
            else:
                scores[bidding_team] -= 6

            if tricks[non_bidding_team] == 0:
                scores[non_bidding_team] -= 6
            else:
                scores[non_bidding_team] += tricks[non_bidding_team]
        return scores


def validate_bid(bid_str, prev, is_dealer):
    if bid_str[-1] in MODIFIERS:
        bid = Bid(bid_str[:-1], bid_str[-1])
    else:
        bid = Bid(bid_str, None)

    if bid.value not in BIDS:
        print("Invalid bid of {}!".format(bid.with_mod()))
    elif bid.value == "pass":
        if prev.value == "pass":
            print("Cannot pass the first bid!")
        else:
            return bid
    elif bid.modifier is not None and bid.value not in BIDS[1:5]:
        print("Bid of {} cannot have a modifier!".format(bid.value))
    elif BIDS.index(bid.value) <= BIDS.index(prev.value) if prev.modifier is None else BIDS.index(prev.bid) - 1:
        print("Bid of {} is too low to beat existing bid of {}!".format(bid.with_mod(), prev.with_mod()))
    elif bid.value == "48" and not (prev.value == "24" and is_dealer):
        print("Cannot Hossenfeffer unless last bid was 24 and you are dealer!")
    else:
        return bid
    return None
