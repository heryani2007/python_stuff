import random

def main():
	color = ["green", "yellow", "red"]
	color_choice = random.choice(color)
	print (color_choice)
	if color_choice == "green":
		print("5 Points Earned")
	elif color_choice == "yellow":
		print ("10 Points Earned")
	else:
		print ("15 Points Earned")

if __name__ == "__main__":
	main()
