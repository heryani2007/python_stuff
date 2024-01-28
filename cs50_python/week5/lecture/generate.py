import random

for _ in range(100):
    choice = random.choice(["heads", "tails"])
    print(choice,end="|")
