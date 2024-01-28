class Guest:
	def __init__(self,name,age,id):
		self.name = name
		self.age = age
		self.id = id
	def greet(self):
		return self.name
		print(f"Hello {self.name}")
	def append(self):
		with open("guest_book.txt","a") as file_object:
			file_object.write(f"{self.name} is {self.age}yo and his id is {self.id}\n")

while True:
	my_guest = Guest(input("Guestname ").title(),input("Age "),input("id "))
	if my_guest() == "exit":
		break
	else:
		my_guest.greet()
		my_guest.append()
