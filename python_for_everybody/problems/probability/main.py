import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            self.contents.extend([ color for i in range(number) ])
        self.original_contents = self.contents[:]

    def draw(self, draws):
        self.contents = self.original_contents[:]
        if draws > len(self.contents):
            return self.contents
        results = random.sample(self.contents, draws)
        for color in results:
            self.contents.remove(color) 
        return results
            


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range(num_experiments):
        results = hat.draw(num_balls_drawn)
        success = True
        for k, v in expected_balls.items():
            if results.count(k) < v:
                success = False
        if success:
            successes += 1
    return successes / num_experiments

