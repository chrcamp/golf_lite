class Golfer:
    """A class for Golfers"""

    def __init__(self, firstname, lastname, email_addr) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email_addr = email_addr

        @property
        def fullname(self):
            return f'{self.firstname} {self.lastname}'
        