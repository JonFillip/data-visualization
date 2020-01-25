from random import choice


class MolecularMotion:
    """A class to simulate motion path of a pollen grain on the surface of a
    drop of water"""
    def __init__(self, num_points=5000):
        """Initialize attributes of class."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    @staticmethod
    def get_step():
        """Get the direction and distance for each grain."""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = distance * direction
        return step

    def fill_path(self):
        """Calculate all the points of motion path"""

        # Keep track of all motion until reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Determine the distance and direction of the pollen path
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
