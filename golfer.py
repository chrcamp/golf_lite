import config
import sqlite3


conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


class Golfer:
    """A class for Golfers"""

    def __init__(self, firstname, lastname, email_addr) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email_addr = email_addr

        @property
        def fullname(self):
            return f'{self.firstname} {self.lastname}'


def golfer_table_init():
    c.execute("""         
              CREATE TABLE IF NOT EXISTS golfers (
                golfer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT
                );
              """)


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


if __name__ == "__main__":

    golfer_table_init()

    golfer_1 = Golfer('Bill', 'Murray', 'TeamZizzou@fakemail.com')
    golfer_2 = Golfer('Mel', 'Brooks', 'spaceballs@theEmail.com')
    golfer_3 = Golfer('NotReal', 'FakeHuman', 'test@invalid.com')
    golfer_4 = Golfer('Larry', 'David', 'noemail@test.com')

    insert_golfer(golfer_1)
    insert_golfer(golfer_2)
    insert_golfer(golfer_3)
    insert_golfer(golfer_4)

    remove_golfer(golfer_3)
    update_golfer_email(golfer_4, 'seinfeld@curb.com')

    c.execute('SELECT * FROM golfers')
    all_golfers = c.fetchall()
    for golfer in all_golfers:
        print(golfer)
