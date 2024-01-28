def main():
	a, b, c = 1, 2, 3
	print(f"a, b, c its as easy as {a}, {b}, {c}")

	first, last = "a,b,c 1,2,3".split(" ")
	print(f"{first} its as easy as {last}")

if __name__ == "__main__":
	main()
