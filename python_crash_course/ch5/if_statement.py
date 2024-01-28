def main():
	num = input("Value: ")
	while True:
		if num != str("10"):
			print(f"{num} is not 10")
			num = input("Value: ")
		else:
			print("Correct")
			break

if __name__ == "__main__":
	main()
