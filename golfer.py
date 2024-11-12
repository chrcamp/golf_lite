import config
import sqlite3
import hashlib
from datetime import datetime


class Golfer:
    """A class for Golfers"""

    def __init__(self, username, password, email, created_at=None, last_login=None, is_active=1, role='user') -> None:
        self.username = username
        self.password = password  # Store as hashed password
        self.email = email
        self.created_at = created_at if created_at else datetime.now()
        self.last_login = last_login
        self.is_active = is_active
        self.role = role


class UserManager:
    def __init__(self, db_path=config.DB_NAME):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("""
                        CREATE TABLE IF NOT EXISTS golfers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            email TEXT UNIQUE,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            last_login TIMESTAMP,
                            is_active INTEGER DEFAULT 1,
                            role TEXT DEFAULT 'user'
                        );
                      """)
            conn.commit()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def create_user(self, username, password, email, role='user'):
        hashed_password = self.hash_password(password)
        new_golfer = Golfer(
            username=username,
            password=hashed_password,
            email=email,
            role=role
        )

        with sqlite3.connect(config.DB_NAME) as conn:
            c = conn.cursor()
            try:
                # Insert the new user into the users table
                c.execute('''
                        INSERT INTO golfers (username, password, email, created_at, last_login, is_active, role) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                    new_golfer.username,
                    new_golfer.password,
                    new_golfer.email,
                    new_golfer.created_at,
                    new_golfer.last_login,
                    new_golfer.is_active,
                    new_golfer.role
                ))
                conn.commit()
                print("User created successfully.")
                return True
            except sqlite3.IntegrityError as e:
                print(f"Error: {e}")
                return False

    def get_user(self, username):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM golfers WHERE username = ?", (username,))
            row = c.fetchone()

            if row:
                return Golfer(
                    username=row[1],
                    password=row[2],
                    email=row[3],
                    created_at=row[4],
                    last_login=row[5],
                    is_active=row[6],
                    role=row[7]
                )
            else:
                print("Golfer not found.")
                return None

    def validate_credentials(self, username, password):
        hashed_password = self.hash_password(password)
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM golfers WHERE username = ?", (username,))
            user = c.fetchone()

            if user:
                stored_hashed_password = user[2]
                if stored_hashed_password == hashed_password:
                    print("Login Successful.")
                    return Golfer(
                        username=user[1],
                        password=user[2],
                        email=user[3],
                        created_at=user[4],
                        last_login=user[5],
                        is_active=user[6],
                        role=user[7]
                )
                else:
                    print("Invalid password.")
                    return False
            else:
                print("Username not found.")
                return False


if __name__ == "__main__":

    user_manager = UserManager()
    user_manager.create_user("test-user", "test123", "test@invalid.com")

    golfer = user_manager.get_user("test-user")
    if golfer:
        print(f"Golfer retrieved: {golfer.username}, {golfer.email}, {golfer.created_at}")
