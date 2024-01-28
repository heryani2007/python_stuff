def main():
	location = ["Japan", "Canada", "Thialand", "France", "Germany"]
	print(location)
	print(sorted(location))
	print(location)
	print(sorted(location, reverse=True))
	print(location)
	location.reverse()
	print(location)
	location.reverse()
	print(location)
	location.sort()
	print(location)
	location.sort(reverse=True)
	print(location)

if __name__ == "__main__":
	main()
