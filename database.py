import sqlite3

from game import Game

class Database:
    def __init__(self):
        self.database = sqlite3.connect("db.sqlite3")
        cur = self.database.cursor()
        cur.execute("DROP TABLE game")
        cur.execute("CREATE TABLE game(id, json)")
        cur.commit()

    def create_game(self, game):
        cur = self.database.cursor()
        cur.execute("SELECT id from game")
        games = map(int, cur.fetchall())
        id = 0 if len(games) == 0 else max(games)  + 1
        cur.execute("INSERT into game VALUES(?, ?)", (str(id), game.to_json()))
        cur.commit()
        return id
    
    def get_game(self, id):
        cur = self.database.cursor()
        cur.execute("SELECT json FROM game WHERE id = ?", str(id))
        json = cur.fetchone()[0]
        return None if len(json) == 0 else Game.from_json(json)
    
    def update_game(self, id, game):
        cur = self.database.cursor()
        cur.execute("UPDATE game SET json = ? WHERE id = ?", (game.to_json(), id))
        cur.commit()
