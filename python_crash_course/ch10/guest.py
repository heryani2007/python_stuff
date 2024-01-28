def guest():
	guestname = input("What is your name: ")
	with open("guest.txt","w") as file_object:
		file_object.write(f"{guestname}\n")

if __name__ == "__name__":
	guest()
