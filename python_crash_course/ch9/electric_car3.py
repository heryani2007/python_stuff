class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def describe_car(self):
		print(f"my {self.make} is a {self.year} model{self.model} it takes gas")

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)

	def describe_car(self):
		print(f"my {self.make} does not take gas")

my_benz = Car("benz", "gla250", "2019")
my_benz.describe_car()

my_tesla = ElectricCar("tesla","y","2019")
my_tesla.describe_car()
