def main():
	list= ["David", "Jacob", "Alan"]
	print(f"Original List: {list}")
	first_pop = list.pop()
	print(f"{first_pop} is uninvited")
	second_pop = list.pop()
	print(f"{second_pop} is uninvited")
	print(f"Poped List: {list} is still invited")

if __name__ == "__main__":
	main()
