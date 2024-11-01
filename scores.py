import config
import sqlite3


conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


class Score:
    # TODO: Fully create, below is only a placeholder
    def __init__(self, strokes):
        self.strokes = strokes


def scores_table_init():
    c.execute("""
              CREATE TABLE IF NOT EXISTS scores (
                score_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER,
                round_id INTEGER,
                hole_id INTEGER,
                golfer_id INTEGER,
                strokes INTEGER,
                putts INTEGER,
                penalties INTEGER DEFAULT 0,
                sand_shots INTEGER DEFAULT 0,
                tee_shot_direction TEXT
              );
            """)


def add_score():
    # TODO: implement
    pass
