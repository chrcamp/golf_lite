import config
import sqlite3
import golf_lite as glf
from customtkinter import *

# Initialize Database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()

# Set appearance and theme
set_appearance_mode("dark")  # Modes: "system" (default), "dark", "light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


if __name__ == '__main__':

    # Initialize database
    glf.golf_lite_init_app()

    # Initialize the UI by showing the welcome screen
    login = glf.Login()
    login.mainloop()

    conn.close()
