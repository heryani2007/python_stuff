class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.modal = model
		self.year = year

	def describe_car(self):
		print(f"My car is a {self.make} model {self.model} year {self.year}")

class Battery:
	def __init__(self,battery_size=75):
		self.battery = battery_size
		print(f"My battery size is {self.battery}")

	def describe_battery(self):
		print(f"My car battery is {self.battery}")

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()

my_tesla = ElectricCar("tesla","y",2019)
my_tesla.battery.describe_battery()
