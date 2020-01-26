from random import randint


class Die:
    """A class representing a single die."""
    def __init__(self, num_side=6):
        """Initialize class attributes. In this case the number of sides of
        the dice is assumed to be 6"""
        self.number_side = num_side

    def roll(self):
        """Return a random value between 1 and the number of sides of the
        dice."""
        return randint(1, self.number_side)
