def read():
	filename = input("Filename: ")
	with open(filename) as file_object:
		words = file_object.read().split()
		print (f"Book: {words[1:9]}")
		print (f"Word Cound: {len(words)}")

if __name__ == "__main__":
	read()
