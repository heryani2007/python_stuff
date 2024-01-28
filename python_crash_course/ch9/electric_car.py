class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def describe_car(self):
		print(f"My car is a {self.make}")

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)

my_tesla = ElectricCar("tesla","x",2019)
my_tesla.describe_car()
