def main():
	list = ["alice","bob","charlie","david","eve","frank","george","hank","irine","jack","kyle","lenny"]
	print(f"The first three items on my list are: {list[:3]}")
	list_middle = len(list)//2
	print (list_middle)
	print(f"Thre items from the middle of the list {list[list_middle:-3]}")
if __name__ == "__main__":
	main()
