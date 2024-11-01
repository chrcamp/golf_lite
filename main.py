import config
import sqlite3
import golf_lite as glf
import course
import golfer
from course import Course
from golfer import Golfer


# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()

glf.golf_lite_init_app()


conn.close()
