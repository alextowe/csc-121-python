class User:
    def __init__(self, first_name, last_name, email, username, password, login_attempts=0):
        """Initialize the user with their first name, last name, email, username, password, and login attempts."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.username = username
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"Name: {self.first_name} {self.last_name}, Email: {self.email}, Username: {self.username}")
        
    def greet_user(self):
        """Greets the user with a personalized message."""
        print(f"Hello, {self.first_name} {self.last_name}!")

alex = User('alex', 'towe', 'alextowe@example.com', 'alextowe', '39807!^*_65@u209*(&(*795)$#%^&')
alex.describe_user()
alex.greet_user()

noah = User('noah', 'person', 'noahperson@example.com', 'noahperson', '33hoih38398*(^)$%&^$HJh%&^$#@!23sh32@#$44g2%^&*')
noah.describe_user()
noah.greet_user()