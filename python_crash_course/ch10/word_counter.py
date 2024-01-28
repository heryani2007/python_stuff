def counter():
	try:
		filename = input("book: ")
		with open(filename) as file_object:
			words = file_object.read()
			words = words.split()
	except FileNotFoundError:
		print ("File Not Found")
	else:
		print(len(words))

if __name__ == "__main__":
	counter()
