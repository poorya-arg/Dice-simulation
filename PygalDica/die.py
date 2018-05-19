from random import randint

class Die():
    """a class for one die"""

    def __init__(self, num_sides = 6):
        """Assume a six_sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value"""
        return randint(1, self.num_sides)
