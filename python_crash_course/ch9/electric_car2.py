class Car:
	def __init__ (self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def describe_car(self):
		print(f"I have a {self.make} {self.model} {self.year}")

class ElectricCar(Car):

	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.voltage = 75
	def describe_electric(self):
		print(f"My {self.make} model{self.model} has a {self.voltage} battery")

my_tesla = ElectricCar("Tesla","Y",2019)
my_tesla.describe_electric()
