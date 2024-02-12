import random
import copy

class Hat:
    """
    Represents a hat containing balls of different colors.

    Attributes:
        contents (list): A list of strings, where each string represents a ball color.
    """

    def __init__(self, **kwargs):
        """
        Creates a Hat object.

        Args:
            kwargs: A dictionary where keys are color names and values are the number of balls
                   of that color.
        """

        self.contents = []
        for color, num_balls in kwargs.items():
            if num_balls >= 0:
                self.contents.extend([color] * num_balls)
            else:
                raise ValueError("Number of balls cannot be negative.")

        if not self.contents:
            raise ValueError("Hat must contain at least one ball.")

    def draw(self, num_balls):
        """
        Draws a random sample of balls from the hat.

        Args:
            num_balls (int): The number of balls to draw.

        Returns:
            list: A list of strings representing the drawn balls.
        """

        if num_balls > len(self.contents):
            return self.contents

        drawn_balls = random.sample(self.contents, num_balls)
        self.contents = [ball for ball in self.contents if ball not in drawn_balls]
        return drawn_balls

def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    """
    Calculates the approximate probability of drawing certain balls from a hat.

    Args:
        hat (Hat): The Hat object representing the hat.
        expected_balls (dict): A dictionary where keys are color names and values are the
                             number of balls of that color to be drawn.
        num_balls_drawn (int): The number of balls to draw in each experiment.
        num_experiments (int): The number of experiments to perform.

    Returns:
        float: The approximate probability as a decimal between 0 and 1.
    """

    success_count = 0
    for _ in range(num_experiments):
        # Create a copy of the Hat to avoid modifying the original
        current_hat = copy.deepcopy(hat)
        drawn_balls = current_hat.draw(num_balls_drawn)

        # Count successes where at least all expected balls are drawn
        success = True
        for color, expected_num in expected_balls.items():
            if drawn_balls.count(color) < expected_num:
                success = False
                break

        success_count += int(success)

    return success_count / num_experiments

# Example usage
hat = Hat(red=5, green=2, blue=4)
probability = experiment(hat=hat,
                  expected_balls={"red":2, "green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print("Probability of drawing at least 2 red balls and 1 green ball:", probability)
