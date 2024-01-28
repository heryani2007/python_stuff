def main():
	animals = []
	i = 0
	while i < 3 :
		animals.append(input(f"pet list: "))
		i += 1
	for _ in animals:
		if _ not in ["dog", "cat"]:
			print(f"A {_} would not make a great pet")
		else:
			print(f"A {_} would make a great pet")
if __name__ == "__main__":
	main()
