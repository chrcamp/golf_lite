import config
import sqlite3

conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


class Course:

    def __init__(self, name, location, nbr_holes, par) -> None:
        self.name = name
        self.location = location
        self.nbr_holes = nbr_holes
        self.par = par


def course_table_init():
    c.execute("""
              CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                course_name TEXT,
                course_location TEXT,
                nbr_holes INTEGER,
                course_par INTEGER
                );
            """)


def insert_course(golfcourse):
    course_search = get_course_by_name(golfcourse.name)
    if len(course_search) == 0:
        with conn:
            c.execute("""INSERT INTO courses (course_name, course_location, nbr_holes, course_par) 
                                VALUES (:name, :location, :holes, :par)""",
                      {
                          'name': golfcourse.name,
                          'location': golfcourse.location,
                          'holes': golfcourse.nbr_holes,
                          'par': golfcourse.par
                      }
                      )
    else:
        print(f"{golfcourse.name} already in table.")


def get_course_by_name(course_name):
    c.execute("SELECT * FROM courses WHERE course_name =:name", {'name': course_name})
    return c.fetchall()


if __name__ == "__main__":

    course_table_init()

    course_1 = Course('Pebble Beach', 'Del Monde Forest, CA', 18, 72)
    course_2 = Course('Bethpage Black Golf Course', 'Old Bethpage, NY', 18, 71)
    course_3 = Course('TPC River Highlands', 'Cromwell, CT', 18, 70)
    course_4 = Course('Racebrook Country Club', 'Orange, CT', 18, 71)

    insert_course(course_1)
    insert_course(course_2)
    insert_course(course_3)
    insert_course(course_4)

    c.execute('SELECT * FROM courses')
    all_courses = c.fetchall()
    for course in all_courses:
        print(course)
