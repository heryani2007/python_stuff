def main():
	students = {}
	for _ in range(3):
		first = input("First: ")
		last = input("Last: ")
		house = input("House: ")
		students[f"first{_}"] = first
		students[f"last{_}"]  = last
		students[f"house{_}"] = house
		print(students)
main()
