def main():
	try:
		num = int(input("A ")) / int(input("B "))
	except ZeroDivisionError:
		print ("No Divide By 0")
	else:
		print(num)

if __name__ == "__main__":
	main()
