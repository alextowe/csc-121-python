class Employee:
    """A class to represent an employee."""
    
    def __init__(self, first_name, last_name, salary):
        """Initialize the employee's name and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def give_raise(self, amount=5000):
        """Add the given amount to the employee's salary."""
        self.salary += amount