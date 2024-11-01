import sqlite3
from course import Course
from golfer import Golfer

conn = sqlite3.connect('golf_lite_data.db')
c = conn.cursor()


def golf_lite_init_app():
    c.execute("""
          CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            course_name TEXT,
            course_location TEXT,
            course_par INTEGER
            );
        """)
    c.execute("""         
          CREATE TABLE IF NOT EXISTS golfers (
            golfer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT
            );
          """)
    c.execute("""          
          CREATE TABLE IF NOT EXISTS holes (
            hole_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER,
            hole_nbr INTEGER,
            hole_par INTEGER,
            hole_distance INTEGER
          );
          """)
    c.execute("""
          CREATE TABLE IF NOT EXISTS rounds (
            round_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER,
            player_id INTEGER,
            tee_color TEXT,
            start_date TEXT
          );
          """)
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


#####
# COURSE TABLE FUNCTIONS
#####
def insert_course(golfcourse):
    course_search = get_course_by_name(golfcourse.name)
    if len(course_search) == 0:
        with conn:
            c.execute("INSERT INTO courses (course_name, course_location, course_par) VALUES (:name, :location, :par)",
                      {
                          'name': golfcourse.name,
                          'location': golfcourse.location,
                          'par': golfcourse.par
                      }
                      )
    else:
        print(f"{golfcourse.name} already in table.")


def get_course_by_name(course_name):
    c.execute("SELECT * FROM courses WHERE course_name =:name", {'name': course_name})
    return c.fetchall()


#####
# GOLFER TABLE FUNCTIONS
#####
def insert_golfer(new_golfer):
    golfer_search = get_golfer_by_email(new_golfer.email_addr)
    if len(golfer_search) == 0:
        with conn:
            c.execute("INSERT INTO golfers (first_name, last_name, email) VALUES (:first, :last, :email)",
                      {
                          'first': new_golfer.firstname,
                          'last': new_golfer.lastname,
                          'email': new_golfer.email_addr
                      }
                      )
    else:
        print("Golfer already in table")


def remove_golfer(golfer_to_remove):
    with conn:
        c.execute("DELETE FROM golfers WHERE email = :email", {'email': golfer_to_remove.email_addr})


def get_golfer_by_email(email):
    c.execute("SELECT * FROM golfers WHERE email = :email", {'email': email})
    return c.fetchall()


def update_golfer_email(golfer_to_update, new_email):
    golfer_search = get_golfer_by_email(new_email)
    if len(golfer_search) == 0:
        with conn:
            c.execute("""UPDATE golfers SET email = :email
                    WHERE first_name = :first AND last_name = :last AND email = :orig_email""",
                      {
                          'email': new_email,
                          'first': golfer_to_update.firstname,
                          'last': golfer_to_update.lastname,
                          'orig_email': golfer_to_update.email_addr
                      }
                      )
    else:
        print("Unable to change email address. Golfer already in table")


#####
# HOLE TABLE FUNCTIONS
#####
def add_hole_to_course(golfcourse, hole_number, hole_par, hole_distance):
    # TODO: implement
    pass


def get_hole_details():
    # TODO: implement
    pass


#####
# ROUNDS TABLE FUNCTIONS
#####
def add_round():
    # TODO: implement
    pass


#####
# SCORES TABLE FUNCTIONS
#####
def add_score():
    # TODO: implement
    pass
