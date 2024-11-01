import config
import sqlite3


conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


class Hole:
    # TODO: Fully create, below is only a placeholder
    def __init__(self, par, distance):
        self.par = par
        self.distance = distance


def holes_table_init():
    c.execute("""          
              CREATE TABLE IF NOT EXISTS holes (
                hole_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER,
                hole_nbr INTEGER,
                hole_par INTEGER,
                hole_distance INTEGER
              );
              """)


def add_hole_to_course():
    # TODO: implement
    pass


def get_hole_details():
    # TODO: implement
    pass
