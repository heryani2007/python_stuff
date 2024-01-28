class Car:
	def __init__ (self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def update_odometer(self,milage):
		self.milage = milage
		print (f"{self.milage}")

	def describe_car(self):
		print(f"I drive an {self.make} {self.model} {self.year}")

if __name__ == "__main__":
	my_car = Car("Mercedes","GLA-250",2019)
	my_car.update_odometer(25)

	my_car.odometer = 23
	print(my_car.odometer)

	my_car.describe_car()
