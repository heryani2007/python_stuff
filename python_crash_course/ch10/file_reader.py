def reader():
	with open("pi_digits.txt") as file_object:
		print (file_object.read().strip(),"end")
reader()
