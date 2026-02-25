class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"\n{self.restaurant_name.title()} is now open!")

sake_sushi = Restaurant('sake sushi', 'japanese')
sake_sushi.describe_restaurant()

taco_bell = Restaurant('taco bell', 'mexican')
taco_bell.describe_restaurant()

burger_king = Restaurant('burger king', 'american')
burger_king.describe_restaurant()