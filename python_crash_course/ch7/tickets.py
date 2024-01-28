def main():
	while True:
		age = input("Age: ")
		if int(age) <= 3:
			print ("free")
		elif 3 < int(age) <= 12:
			print("$10")
		elif int(age) > 12:
			print ("$15")
		elif str(age) == "quit":
			break

if __name__ == "__main__":
	main()
