def main():
	list = ["alice", "bob", "charlie"]
	for _ in list:
		if _ == "alice":
			print ("Hello Alice")
		else:
			print (f"{_} is not Alice")

if __name__ == "__main__":
	main()
