from random import choice

class Exercise:
    """
    Represents the type of exercise the user will perform.

    attributes: muscle, name, time
    """
    def __init__(self, muscle, time):
        self.muscle = muscle
        self.name = random.choice(muscle)
        self.time = time
        workout = []