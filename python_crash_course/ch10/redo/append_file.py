def append():
	filename = input("Filename ")
	with open(filename,"a") as file_object:
		file_object.write(input("Line\n")+"\n")
append()
