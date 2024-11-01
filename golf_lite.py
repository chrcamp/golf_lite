import config
import sqlite3
import course
import golfer
import holes
import rounds
import scores

conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


def golf_lite_init_app():
    """
    Initialize database tables.
    """
    course.course_table_init()
    golfer.golfer_table_init()
    rounds.rounds_table_init()
    scores.scores_table_init()
    holes.holes_table_init()
