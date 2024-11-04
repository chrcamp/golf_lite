import config
import sqlite3
import golf_lite as glf
from customtkinter import *

# Initialize Database
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()
glf.golf_lite_init_app()

# Set appearance and theme
set_appearance_mode("dark")  # Modes: "system" (default), "dark", "light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Initialize Main Window
window = CTk()
window.title("Golf Lite App")
window.geometry('1200x700+0+0')


# Define welcome screen function
def show_welcome_screen():
    # Clear existing widgets
    for widget in window.winfo_children():
        widget.destroy()

    # Welcome Label
    label_welcome = CTkLabel(window, text="Welcome to Golf Lite", font=("Avenir", 36), text_color='light green')
    label_welcome.pack(pady=80)

    # Enter App Button
    button_enter_app = CTkButton(window, text="Enter App", command=show_main_screen)
    button_enter_app.pack()


def show_main_screen():
    # Clear existing widgets
    for widget in window.winfo_children():
        widget.destroy()

    # Main Screen Contents
    header = CTkFrame(window, fg_color="transparent")
    header.pack(side='top', fill='x')

    label_main = CTkLabel(header, text="Golf Lite", font=("Avenir", 24), text_color='light green')
    label_main.pack(side='left', padx=10, pady=20)
    exit_button = CTkButton(header, text="Quit App", command=window.destroy)
    exit_button.pack(side='right', padx=10)

    button_new_golfcourse = CTkButton(window, text="Add New Course", command=add_new_course_form)
    button_new_golfcourse.pack(pady=80)


def add_new_course_form():
    for widget in window.winfo_children():
        widget.destroy()

    # Header
    header = CTkFrame(window, fg_color="transparent")
    header.pack(side='top', fill='x')
    label_new_course = CTkLabel(header, text="Add New Course", font=("Avenir", 18), text_color='light green')
    label_new_course.pack(side='top', pady=20)

    # Form Contents
    input_course_name = CTkEntry(window, placeholder_text='Course Name')
    input_course_name.pack()
    input_course_location = CTkEntry(window, placeholder_text='Course Location')
    input_course_location.pack()

    # Footer
    footer = CTkFrame(window, width=200, fg_color="transparent")
    footer.pack(side='bottom')
    button_cancel = CTkButton(footer, text="Cancel", command=show_main_screen)
    button_cancel.pack(side='left', padx=10, pady=20)
    button_add_course = CTkButton(footer, text="Add Course")
    button_add_course.pack(side='right', padx=10, pady=20)


# Initialize the UI by showing the welcome screen
show_welcome_screen()

# Run the app
window.mainloop()
conn.close()
