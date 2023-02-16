import sqlite3

from game import Game


class Database:
    def __init__(self):
        self.database = sqlite3.connect("db.sqlite3")
        cur = self.database.cursor()
        try:
            cur.execute("DROP TABLE game")
        except sqlite3.OperationalError:
            print("no table found") # TODO: Improve error message here?
        cur.execute("CREATE TABLE game(id, json)")
        self.database.commit()

    def create_game(self):
        cur = self.database.cursor()
        cur.execute("SELECT id from game")
        games = set(map(int, cur.fetchall()))
        id = 0 if len(games) == 0 else max(games) + 1
        game = Game(id=id)
        cur.execute("INSERT into game VALUES(?, ?)", (str(id), game.to_json()))
        self.database.commit()
        return game
    
    def get_game(self, id):
        cur = self.database.cursor()
        cur.execute("SELECT json FROM game WHERE id = ?", str(id))
        json = cur.fetchone()[0]
        return None if len(json) == 0 else Game(json_string=json)
    
    def update_game(self, game):
        cur = self.database.cursor()
        cur.execute("UPDATE game SET json = ? WHERE id = ?", (game.to_json(), str(game.game_id)))
        self.database.commit()
