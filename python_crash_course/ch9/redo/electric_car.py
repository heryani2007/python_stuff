class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
	def odometer(self,odometer):
		print(f"I have a {self.make} {self.model} {self.year} the milage is {odometer}")

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)

	def voltage(self,volt):
		print(f"I have a {self.make} {self.model} {self.year} it has a {volt} volt battery")

my_car = Car("Merc","GLA",2019)

my_tesla = ElectricCar("Tesla","Model Y", 2019)

my_tesla.voltage(3000)
