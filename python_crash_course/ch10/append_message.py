def append():
	filename = "programming.txt"
	with open(filename,"a") as file_object:
		file_object.write("I also like C\n")

append()
