class Die:
    """A class representing a single die."""
    def __init__(self, sides=6):
        """Initialize the die with a default of 6 sides."""
        self.sides = sides

    def roll_die(self):
        """Simulate rolling the die and return a random number between 1 and the number of sides."""
        import random
        return random.randint(1, self.sides)

die_sizes = [6, 10, 20]
for size in die_sizes:
    die = Die(sides=size)
    numbers = []
    for roll in range(10):
        numbers.append(die.roll_die())
    print(f"\n{size}-sided die rolls: {numbers}")