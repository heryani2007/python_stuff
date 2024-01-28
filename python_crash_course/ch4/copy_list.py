def main():
	list = ["alice", "bob", "charlie", "david", "eve"]
	print (f"List1: {list}")
	list2 = list[:]
	print (f"List2: {list2}")
	list3 = list
	print (f"List3: {list3}")
	list[0] = "amy"
	print ()
	print (f"Modified List1: {list}")
	print (f"pass_by_value: {list2}")
	print (f"pass_by_reference: {list3}")


if __name__ == "__main__":
	main()
