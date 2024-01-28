def main():
	list = []
	for _ in range(2):
		list.append(input("Value: "))
	if list[0] == 1 or list[0] == 2:
		print ("Condition Met")
	else:
		print ("Condition Fail")
if __name__ == "__main__":
	main()
