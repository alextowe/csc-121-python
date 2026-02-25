from modules.user import User

class Admin(User):
    """Represent an admin user."""
    def __init__(self, first_name, last_name, email, username, password, login_attempts=0):
        """Initialize the admin user with their information and privileges."""
        super().__init__(first_name, last_name, email, username, password, login_attempts)
        self.privileges = Privileges()

class Privileges:
    """Represent the privileges of an admin user."""
    def __init__(self, privileges=[]):
        """Initialize the privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the admin user."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"{privilege}")
