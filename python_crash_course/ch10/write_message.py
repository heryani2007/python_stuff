def writer():
	filename = "programming.txt"
	with open(filename,"w") as file_object:
		file_object.write("I like programming\n")

writer()
