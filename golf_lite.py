import config
import sqlite3
import course
import golfer
import holes
import rounds
import scores
from customtkinter import *
from datetime import datetime as dt

user_manager = golfer.UserManager()
conn = sqlite3.connect(config.DB_NAME)
c = conn.cursor()


def golf_lite_init_app():
    """Initialize database tables."""
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
        self.bind('<Return>', self.attempt_login)

        label_or = CTkLabel(self, text="--OR--")
        label_or.pack()
        button_register = CTkButton(self, text='Register Golfer', command=self.open_registration)
        button_register.pack()

    def attempt_login(self, event=None):
        username = self.entry_username.get()
        password = self.entry_password.get()
        valid_user = user_manager.validate_credentials(username, password)
        if valid_user:
            self.open_main_app(valid_user)
        else:
            self.create_widgets()
            label_failed_login = CTkLabel(self, text='Login attempt failed.', text_color='red')
            label_failed_login.pack()

    def open_main_app(self, user):
        self.destroy()
        app = App(user)
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

        button_back_to_login = CTkButton(self, text="Back to Login", command=self.exit_to_login)
        button_back_to_login.pack(pady=10)

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

    def process_user_creation(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()

        valid_new_user = user_manager.create_user(username, password, email)

        if valid_new_user:
            label_new_user_success = CTkLabel(self, text='Golfer created successfully.', text_color='light green')
            label_new_user_success.pack()
        else:
            self.create_widgets()
            label_new_user_failed = CTkLabel(self, text='Username not available', text_color='red')
            label_new_user_failed.pack()

    def exit_to_login(self):
        self.destroy()
        login = Login()
        login.mainloop()


class App(CTk):
    def __init__(self, golfer: golfer.Golfer):
        super().__init__()
        self.golfer = golfer
        self.title("Golf Lite App")
        window_width, window_height = 1200, 700
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_pos = (screen_width // 2) - (window_width // 2)
        y_pos = (screen_height // 2) - (window_height // 2)
        self.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')
        self.create_widgets()

    def exit_to_login(self):
        self.destroy()
        login = Login()
        login.mainloop()

    def create_toolbar(self):
        toolbar = CTkFrame(self)
        toolbar.pack(side='left', fill='y')
        label_user = CTkLabel(toolbar, text=self.golfer.username, font=("Avenir", 18), text_color="light green")
        label_user.pack(side='top', padx=5, pady=20)
        button_home = CTkButton(toolbar, text="Home", command=self.create_widgets)
        button_home.pack(pady=(10, 20))

        button_new_round = CTkButton(toolbar, text="Enter New Round", command=None)
        button_new_round.pack(pady=5)
        button_view_rounds = CTkButton(toolbar, text="View Rounds", command=None)
        button_view_rounds.pack(pady=5)
        button_new_golfcourse = CTkButton(toolbar, text="Add New Course", command=self.add_new_course_form)
        button_new_golfcourse.pack(pady=5)

        # Log Off / Quit
        frame_exit = CTkFrame(toolbar)
        frame_exit.pack(side='bottom')
        button_user_profile = CTkButton(frame_exit, text="User Profile", command=self.view_user_profile)
        button_user_profile.pack(pady=(5, 10))
        logoff_button = CTkButton(frame_exit, text="Log Off", command=self.exit_to_login)
        logoff_button.pack(pady=5)
        exit_button = CTkButton(frame_exit, text="Quit App", command=self.destroy)
        exit_button.pack(padx=5, pady=(5, 10))

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_toolbar()

        # Header
        header = CTkFrame(self, fg_color="transparent")
        header.pack(side='top', fill='x')
        label_main = CTkLabel(header, text="Golf Lite", font=("Avenir", 24), text_color='light green')
        label_main.pack(pady=20)

        # Content
        future_content = CTkLabel(self, text="App Content Coming Soon!!", font=("Avenir", 36), text_color="light green")
        future_content.pack(pady=80)

    def view_user_profile(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_toolbar()

        # Header
        header = CTkFrame(self, fg_color="transparent")
        header.pack(side='top', fill='x')
        label_page = CTkLabel(header, text="User Profile", font=("Avenir", 24), text_color='light green')
        label_page.pack(pady=20)

        # Content
        profile_data = {
            "Username": self.golfer.username,
            "Email": self.golfer.email,
            "User Since": dt.strptime(self.golfer.created_at, '%Y-%m-%d %H:%M:%S.%f').strftime("%m/%d/%Y"),
            "Last Login": dt.strptime(self.golfer.last_login, '%Y-%m-%d %H:%M:%S.%f').strftime("%x %X")
        }

        frame_profile = CTkFrame(self)
        frame_profile.pack(pady=80)

        for row, (field_name, field_value) in enumerate(profile_data.items()):
            name_label = CTkLabel(frame_profile, text=field_name, anchor="e")
            name_label.grid(row=row, column=0, padx=5, pady=10, sticky="e")
            value_label = CTkLabel(frame_profile, text=field_value, anchor="w")
            value_label.grid(row=row, column=1, padx=5, pady=10, sticky="w")

        button_change_pw = CTkButton(self, text="Change Password", command=self.view_change_pw)
        button_change_pw.pack()

    def view_change_pw(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_toolbar()
        header = CTkFrame(self, fg_color="transparent")
        header.pack(side='top', fill='x')
        label_page = CTkLabel(header, text="Change Password", font=("Avenir", 24), text_color='light green')
        label_page.pack(pady=20)

        form = CTkFrame(self, fg_color="transparent")
        form.pack(pady=80)

        label_new_pw = CTkLabel(form, text="New Password: ", font=("Avenir", 16), text_color='light green', anchor="e")
        label_new_pw.grid(row=0, column=0, padx=5, sticky="e")
        self.entry_new_pw = CTkEntry(form, width=140, show="*")
        self.entry_new_pw.grid(row=0, column=1)
        label_repeat_pw = CTkLabel(form, text="Repeat New Password: ", font=("Avenir", 16), text_color='light green', anchor="e")
        label_repeat_pw.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_repeat_pw = CTkEntry(form, width=140, show="*")
        self.entry_repeat_pw.grid(row=1, column=1)

        button_cancel = CTkButton(form, text="Cancel", command=self.view_user_profile)
        button_cancel.grid(row=2, column=0, padx=10, pady=20)
        button_submit = CTkButton(form, text="Submit", command=self.attempt_pw_change)
        button_submit.grid(row=2, column=1, padx=10)

    def attempt_pw_change(self):
        new_pw = self.entry_new_pw.get()
        repeat_pw = self.entry_repeat_pw.get()
        if new_pw == repeat_pw:
            user_manager.change_password(self.golfer.username, new_pw)
            self.view_change_pw()
            label_pw_change_success = CTkLabel(self, text='Password changed successfully.', text_color='light green')
            label_pw_change_success.pack()
        else:
            self.view_change_pw()
            label_pw_change_failed = CTkLabel(self, text='PW Entries do not match', text_color='red')
            label_pw_change_failed.pack()

    def add_new_course_form(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_toolbar()

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
        # TODO: implement new course creation
