import random

list = list(range(1,9))
choice_counter = []
counter_count = {}
for _ in range(100):
	choice = random.choice(list)
#	print(choice, end=" | ")
	choice_counter.append(choice)
for _ in choice_counter:
	counter_count[_] = choice_counter.count(_)

ordered = sorted(counter_count)
print (ordered)
print()
