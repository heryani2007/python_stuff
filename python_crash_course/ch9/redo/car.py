class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
	def odometer(self,odometer):
		print(f"I have a {self.make} {self.model} {self.year} the milage is {odometer}")

my_car = Car("Merc","GLA",2019)
my_car.odometer(29_000)
