import config
import sqlite3
import course
import golfer
import holes
import rounds
import scores
from golfer import UserManager
from customtkinter import *

user_manager = UserManager()
conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


def golf_lite_init_app():
    """
    Initialize database tables.
    """
    user_manager = UserManager()
    course.course_table_init()
    rounds.rounds_table_init()
    scores.scores_table_init()
    holes.holes_table_init()


class Login(CTk):
    def __init__(self):
        super().__init__()
        self.entry_password = None
        self.entry_username = None
        self.title('⛳️ Golf Lite - Login')
        window_width, window_height = 600, 350
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_pos = (screen_width // 2) - (window_width // 2)
        y_pos = (screen_height // 2) - (window_height // 2)

        self.attributes('-topmost', True)
        self.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')
        self.create_widgets()

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        label_welcome = CTkLabel(self, text="Welcome to Golf Lite", font=("Avenir", 36), text_color='light green')
        label_welcome.pack(side='top', pady=10)

        label_username = CTkLabel(self, text='Username')
        label_username.pack()
        self.entry_username = CTkEntry(self)
        self.entry_username.pack(pady=(0, 10))

        label_password = CTkLabel(self, text='Password')
        label_password.pack()
        self.entry_password = CTkEntry(self, show='*')
        self.entry_password.pack(pady=(0, 20))

        button_enter_app = CTkButton(self, text="Log in", command=self.attempt_login)
        button_enter_app.pack(pady=(0, 20))

        label_or = CTkLabel(self, text="--OR--")
        label_or.pack()
        button_register = CTkButton(self, text='Register Golfer', command=self.open_registration)
        button_register.pack()

    def attempt_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        valid_login = user_manager.validate_credentials(username, password)
        if valid_login:
            print(username, password)
            self.open_main_app()
        else:
            self.create_widgets()
            label_failed_login = CTkLabel(self, text='Login attempt failed.', text_color='red')
            label_failed_login.pack()

    def open_main_app(self):
        self.destroy()
        app = App()
        app.mainloop()

    def open_registration(self):
        self.destroy()
        register = Register()
        register.mainloop()


class Register(CTk):
    def __init__(self):
        super().__init__()
        self.title("Golf Lite - Register New Golfer")
        window_width, window_height = 600, 400
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_pos = (screen_width // 2) - (window_width // 2)
        y_pos = (screen_height // 2) - (window_height // 2)
        self.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')
        self.create_widgets()

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        label_register = CTkLabel(self, text="Register New Golfer", font=("Avenir", 36), text_color='light green')
        label_register.pack(side='top', pady=10)

        label_username = CTkLabel(self, text='Username')
        label_username.pack()
        self.entry_username = CTkEntry(self)
        self.entry_username.pack(pady=(0, 10))

        label_password = CTkLabel(self, text='Password')
        label_password.pack()
        self.entry_password = CTkEntry(self, show='*')
        self.entry_password.pack(pady=(0, 10))

        label_email = CTkLabel(self, text='Email Address')
        label_email.pack()
        self.entry_email = CTkEntry(self)
        self.entry_email.pack(pady=(0, 20))

        button_register = CTkButton(self, text='Register', command=self.process_user_creation)
        button_register.pack()
        # TODO: actually register new golfer

    def process_user_creation(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()

        valid_new_user = user_manager.create_user(username, password, email)

        if valid_new_user:
            self.destroy()
            login = Login()
            login.mainloop()
            label_new_user_success = CTkLabel(self, text='Golfer created successfully.', text_color='light green')
            label_new_user_success.pack()
        else:
            self.create_widgets()
            label_new_user_failed = CTkLabel(self, text='Username not available', text_color='red')
            label_new_user_failed.pack()


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Golf Lite App")
        window_width, window_height = 1200, 700
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_pos = (screen_width // 2) - (window_width // 2)
        y_pos = (screen_height // 2) - (window_height // 2)
        self.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')
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
