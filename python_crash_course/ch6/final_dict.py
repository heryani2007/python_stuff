def main():
	students = {"name" :"Harry", "house":"Gryffindor", "patronus":"Stag"}
	print (students)

	for key,value in students.items():
		print(f"{key}")
		print(f"{value}")

	for _ in range(2):
		students[f"name{_}"] = input("Name: ")
		students[f"house{_}"] = input("House: ")
		students[f"patronus{_}"] = input("Patronus: ")
	print (students)

if __name__ == "__main__":
	main()
