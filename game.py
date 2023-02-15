import json

class Game:

    def __init__(self, id, players):
        self.game_id = id # TODO: allow multiple games
        self.players = players
        self.scores = [0, 0]
        self.bidding = True
        self.dealer = 0
        self.acting_player = 0
        self.trick = [""] * 4

    def __init__(self, data):
        data = json.loads(data)
        self.game_id = data["game_id"]
        self.players = data["players"]
        self.scores = data["scores"]
        self.bidding = data["bidding"]
        self.dealer = data["dealer"]
        self.acting_player = data["acting_player"]
        self.trick = data["trick"]

    @staticmethod
    def from_json(data):
        return json.loads(data)

    def to_json(self):
        return json.dumps({
            "game_id": self.game_id,
            "players": self.players,
            "scores": self.scores,
            "bidding": self.bidding,
            "dealer": self.dealer,
            "acting_player": self.acting_player,
            "trick": self.trick
        }, sort_keys=True)
    

    def json_for_player(self, player_id):
        return json.dumps({
            "game_id": self.game_id,
            "player_id": player_id,
            "player": self.players[player_id].json(),
            "scores": self.scores,
            "bidding": self.bidding,
            "dealer": self.dealer,
            "acting_player": self.acting_player,
            "trick": self.trick
        }, sort_keys=True)
