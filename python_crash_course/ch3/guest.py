def main():
	guest_list = ["me", "myself", "I"]
	for index,guest in enumerate(guest_list):
		print(f"my {index+1} guest is {guest}")
	print(f"{guest_list[2]} cannot make it")
	guest_list[2] = "none"
	print(f"New list {guest_list}") 
if __name__ == "__main__":
	main()
