class Player:

    def __init__(self):
        self.hand = []

    def to_json(self):
        return json.dumps({
            "hand": self.hand
        }, sort_keys=True)
    