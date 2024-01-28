import random

numbers = list(range(1,1000))

chosen_number = random.choice(numbers)
print(chosen_number)
while True:
	guess = int(input("Guess: "))
	if guess == chosen_number:
		print ("Correct")
		break
	else:
		print ("Incorrect")
