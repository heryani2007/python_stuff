def main():
	pizza = ["peppironni", "cheese", "pinaple"]
	for _ in pizza:
		if _ in ["peppironni", "cheese"]:
			print(f"I love {_} pizza")
		if _ == "pinaple":
			print(f"I hate {_} pizza")
	print(f"I really love pizza")
if __name__ == "__main__":
	main()
