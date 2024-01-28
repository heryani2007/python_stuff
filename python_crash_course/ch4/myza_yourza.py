def main():
	my_pizza = ["cheese","meat","veg"]
	your_pizza = my_pizza[:]
	my_pizza.append("pinapple")
	your_pizza.append("shrimp")
	print(my_pizza)
	print(your_pizza)

	for _ in my_pizza[1]:
		print (_,end="")
	print()
	for _ in your_pizza[1]:
		print (_,end="")
	print()

if __name__ == "__main__":
	main()
