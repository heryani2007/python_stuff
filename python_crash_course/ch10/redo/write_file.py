def write():
	filename = input("Filename: ")
	with open(filename, "w") as file_object:
		file_object.write(input("First Line: \n")+"\n")
		file_object.write(input("Second Line\n")+"\n")

if __name__ == "__main__":
	write()
