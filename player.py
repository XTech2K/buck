class Player:

    def __init__(self):
        self.hand = []

    def json(self):
        return json.dumps({
            "hand": self.hand
        }, sort_keys=True)
    