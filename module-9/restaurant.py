class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"\n{self.restaurant_name.title()} is now open!")

restaurant = Restaurant('Olive Garden', 'Italian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
