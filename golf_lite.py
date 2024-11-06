import config
import sqlite3
import course
import golfer
import holes
import rounds
import scores
from customtkinter import *


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


class Login(CTk):
    def __init__(self):
        super().__init__()
        self.entry_password = None
        self.entry_username = None
        self.title('⛳️ Golf Lite - Login')
        # self.overrideredirect(True)  # removes title bar
        self.geometry('600x300+0+0')
        self.create_widgets()

    def create_widgets(self):
        label_welcome = CTkLabel(self, text="Welcome to Golf Lite", font=("Avenir", 36), text_color='light green')
        label_welcome.pack(side='top', pady=10)

        label_username = CTkLabel(self, text='Username / Email')
        label_username.pack()
        self.entry_username = CTkEntry(self)
        self.entry_username.pack(pady=(0, 10))

        label_password = CTkLabel(self, text='Password')
        label_password.pack()
        self.entry_password = CTkEntry(self, show='*')
        self.entry_password.pack(pady=(0, 20))

        button_enter_app = CTkButton(self, text="Log in", command=self.verify_credentials)
        button_enter_app.pack()

        label_failed_login = CTkLabel(self, text='Login attempt failed.', text_color='red')
        label_failed_login.pack()

    def verify_credentials(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # TODO: Add logic
        if True:
            print(username, password)
            self.open_main_app()

    def open_main_app(self):
        self.destroy()
        app = App()
        app.mainloop()


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Golf Lite App")
        self.geometry('1200x700+0+0')
        self.create_widgets()

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Header
        header = CTkFrame(self, fg_color="transparent")
        header.pack(side='top', fill='x')
        label_main = CTkLabel(header, text="Golf Lite", font=("Avenir", 24), text_color='light green')
        label_main.pack(side='left', padx=10, pady=20)
        exit_button = CTkButton(header, text="Quit App", command=self.destroy)
        exit_button.pack(side='right', padx=10)

        # Content
        button_new_golfcourse = CTkButton(self, text="Add New Course", command=self.add_new_course_form)
        button_new_golfcourse.pack(pady=80)

    def add_new_course_form(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Header
        header = CTkFrame(self, fg_color="transparent")
        header.pack(side='top', fill='x')
        label_new_course = CTkLabel(header, text="Add New Course", font=("Avenir", 18), text_color='light green')
        label_new_course.pack(side='top', pady=20)

        # Form Contents
        input_course_name = CTkEntry(self, placeholder_text='Course Name')
        input_course_name.pack()
        input_course_location = CTkEntry(self, placeholder_text='Course Location')
        input_course_location.pack()

        # Footer
        footer = CTkFrame(self, width=200, fg_color="transparent")
        footer.pack(side='bottom')
        button_cancel = CTkButton(footer, text="Cancel", command=self.create_widgets)
        button_cancel.pack(side='left', padx=10, pady=20)
        button_add_course = CTkButton(footer, text="Add Course")
        button_add_course.pack(side='right', padx=10, pady=20)
