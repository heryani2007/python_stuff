def counter():
	files = ["alice.txt","1984.txt","moby.txt", "yan.txt"]
	for file in files:
		try:
			with open(file) as file_object:
				words = file_object.read()
				words = words.split()
		except FileNotFoundError:
			print ("File Not Found")
		else:
			print (len(words))
if __name__ == "__main__":
	counter()
