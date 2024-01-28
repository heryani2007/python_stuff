def main():
	orders = ["pastrami","cheese steak", "roast beef", "italian"]
	done = []
	print (orders)
	print ("making order")

	while orders:
		order = orders.pop()
		done.append(order)
	print (f"Remaining : {orders}")
	print (f"Completed : {done}")

if __name__ == "__main__":
	main()
