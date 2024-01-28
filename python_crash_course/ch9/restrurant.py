class Resturant:
	def __init__(self,name,type):
		self.name = name
		self.type = type

	def announce(self):
		print(f"{self.name} is a {self.type} resturant")

my_resturant = Resturant("julios","Mexican")
my_resturant.announce()
