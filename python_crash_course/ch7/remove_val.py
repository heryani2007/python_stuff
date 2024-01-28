'''
def main():
	pets = ["cat","dog","rabbit","cat"]
	print (pets)
	for _ in pets:
		pets.remove("cat")
	print (pets)
if __name__ == "__main__":
	main()
'''

def main():
	pets = ["cat","dog","rabbit","cat"]
	while "cat" in pets:
		pets.remove("cat")
	print (pets)
main()
