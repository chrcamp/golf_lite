import golf_lite as glf
from customtkinter import *


# Set appearance and theme
set_appearance_mode("dark")  # Modes: "system" (default), "dark", "light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Initialize database
glf.golf_lite_init_app()

# Initialize the UI by showing the welcome screen
login = glf.Login()
login.mainloop()
