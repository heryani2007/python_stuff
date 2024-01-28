class Resturant:
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.served = 0

	def describe(self):
		print(f"{self.name} is a {self.type} resturant")

	def open(self):
		print(f"{self.name} is now open")

	def set_served(self,number):
		self.served = number
		print(f"Value set through method: {self.served}")

	def increment_served(self,number):
		print("Value incremented through method: ", self.served + number)

resturant = Resturant("Black Bear","Diner")
print("Original Value:", resturant.served)
resturant.served = 5
print("Value Modified Directly: ", resturant.served)
resturant.set_served(10)
resturant.increment_served(5)
