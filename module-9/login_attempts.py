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

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0

alex = User('alex', 'towe', 'alextowe@example.com', 'alextowe', '39807!^*_65@u209*(&(*795)$#%^&', login_attempts=4)
print(f"Login attempts: {alex.login_attempts}")

alex.increment_login_attempts()
alex.increment_login_attempts()
alex.increment_login_attempts()
alex.increment_login_attempts()
print(f"Login attempts after incrementing: {alex.login_attempts}")

alex.reset_login_attempts()
print(f"Login attempts after resetting: {alex.login_attempts}")