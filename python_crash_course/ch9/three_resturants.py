class Resturant:
	def __init__(self,name,type):
		self.name = name
		self.type = type

	def describe_resturant(self):
		print(f"{self.name} is a {self.type} resturant")

	def open_resturant(self):
		print(f"{self.name} is open")

rest1 = Resturant("Luigi","Italian")
rest2 = Resturant("Maries","French")
rest3 = Resturant("Alexandrios","Spanish")

rest1.describe_resturant()
rest1.open_resturant()
rest2.describe_resturant()
rest2.open_resturant()
rest3.describe_resturant()
rest3.open_resturant()
