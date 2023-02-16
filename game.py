import json

from bid import modifier
from deck import deal
from player import Player


class Game:

    def __init__(self, id=None, json_string=None):

        if id is not None:
            self.game_id = id
            self.names = ['0', '1', '2', '3'] # TODO: allow players to name themselves 
            self.scores = [0, 0]
            self.dealer = None
            self.reset_round()

        elif json_string is not None:
            data = json.loads(json_string)
            for key in data:
                setattr(self, key, data[key])
        
        else:
            raise TypeError

    def reset_round(self):
        self.dealer = (self.dealer + 1) % 4 if self.dealer else 0
        self.highest_bidder = None
        self.active_player = None
        self.bidding = True
        self.bids = [None] * 4
        self.leader = None
        self.hands = deal()
        self.tricks = [[None] * 4 for _ in range(6)]
        self.taken = [0, 0]

    def to_json(self, player_id=None, pretty=False):
        d = vars(self).copy()
        if player_id:
            d.pop("hands")
            d["player_id"] = player_id
            d["hand"] = self.hands[player_id]
        if pretty:
            return json.dumps(d, sort_keys=True, indent=2)
        else:
            return json.dumps(d, sort_keys=True)

    def winning_bid(self): # TODO: make property?
        return self.bids[self.highest_bidder] if self.highest_bidder is not None else None
