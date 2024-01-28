def main():
	banned_users = []
	for _ in range(3):
		banned_users.append(input("Banned UserName: "))
	if "bob" in banned_users:
		print ("Bob is banned")
	else:
		print ("Bob not in list", end = " ")
		for _ in banned_users:
			print(f"{_}",end=" .")
		print()

if __name__ == "__main__":
	main()
