import config
import sqlite3


conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


class Round:
    # TODO: Fully create, below is only a placeholder
    def __init__(self, tee_color):
        self.tee_color = tee_color


def rounds_table_init():
    c.execute("""
              CREATE TABLE IF NOT EXISTS rounds (
                round_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER,
                player_id INTEGER,
                tee_color TEXT,
                start_date TEXT
              );
              """)


def add_round():
    # TODO: implement
    pass
