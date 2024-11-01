import config
import sqlite3

conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


class Hole:
    # TODO: Fully create, below is only a placeholder
    def __init__(self, course_id, hole_nbr, par, distance):
        self.course_id = course_id
        self.hole_nbr = hole_nbr
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


def insert_hole(hole: Hole):
    with conn:
        c.execute("""INSERT INTO holes (course_id, hole_nbr, hole_par, hole_distance)
        VALUES (:course_id, :nbr, :par, :distance)""",
                  {
                      'course_id': hole.course_id,
                      'nbr': hole.hole_nbr,
                      'par': hole.par,
                      'distance': hole.distance
                  }
                  )


def get_hole_details():
    # TODO: implement
    pass


if __name__ == "__main__":
    test_hole = Hole(6, 1, 4, 445)
    insert_hole(test_hole)
