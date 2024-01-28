import random
class Randomwalk:
    def __init__(self,steps=5000):
        self.steps = steps
        self.x_values = [0]
        self.y_values = [0]
    def walk(self):
        while len(self.x_values) < self.steps:
            x_direction = random.choice([-1,1])
            x_distance = random.choice([1,2,3,4,5])
            x_step = x_direction * x_distance

            y_direction = random.choice([-1,1])
            y_distance = random.choice([1,2,3,4,5])
            y_step = y_direction * y_distance

            if x_step == 0 or y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

