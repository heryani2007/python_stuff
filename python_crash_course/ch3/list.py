def main():
	simple_list = ["this", "is", "cs", 50, "list"]
	print("List no loop")
	print(simple_list)

	print()
	print("For loop standard")
	for _ in simple_list:
		print (_)

	print()
	print("For loop no \\n with end=''")
	for _ in simple_list:
		print(_,end=" ")
	print()

if __name__ == "__main__":
	main()
