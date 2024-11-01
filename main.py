import sqlite3
import golf_lite as glf
from course import Course
from golfer import Golfer


# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('golf_lite_data.db')
c = conn.cursor()

glf.golf_lite_init_app()

course_1 = Course('Pebble Beach', 'Del Monde Forest, CA', 72)
course_2 = Course('Bethpage Black Golf Course', 'Old Bethpage, NY', 71)
course_3 = Course('TPC River Highlands', 'Cromwell, CT', 70)

glf.insert_course(course_1)
glf.insert_course(course_2)
glf.insert_course(course_3)
glf.insert_course(course_2)

c.execute('SELECT * FROM courses')
all_courses = c.fetchall()
for course in all_courses:
    print(course)

golfer_1 = Golfer('Bill', 'Murray', 'TeamZizzou@fakemail.com')
golfer_2 = Golfer('Mel', 'Brooks', 'spaceballs@theEmail.com')
golfer_3 = Golfer('NotReal', 'FakeHuman', 'test@invalid.com')
golfer_4 = Golfer('Larry', 'David', 'noemail@test.com')

glf.insert_golfer(golfer_1)
glf.insert_golfer(golfer_2)
glf.insert_golfer(golfer_3)
glf.insert_golfer(golfer_4)

c.execute('SELECT * FROM golfers')
all_golfers = c.fetchall()
for golfer in all_golfers:
    print(golfer)

glf.remove_golfer(golfer_3)
glf.update_golfer_email(golfer_4, 'seinfeld@test.com')


conn.close()
