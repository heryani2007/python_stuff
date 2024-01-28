import json
def main():
	with open("numbers.json") as file_object:
		numbers = json.load(file_object)
	print(numbers)

if __name__ == "__main__":
	main()
