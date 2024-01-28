def main():
	guest_list = ["David", "John", "Alan"]
	print(f"First List: {guest_list}")
	guest_list.insert(0, "First")
	guest_list.append("Last")
	mid = len(guest_list)/2
	guest_list.insert(int(mid), "Mid")
	print(f"Final List: {guest_list}")

if __name__ == "__main__":
	main()
