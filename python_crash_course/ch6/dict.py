dictionary = {"Harry":"Gryffindor", "Hermoine":"Gryffindor", "Ron":"Gryffindor"}
print(dictionary["Ron"])
for key,value in dictionary.items():
	print (f"{key} is in {dictionary[key]} {value}")

for _ in dictionary:
	print ("Second For Loop ", _)
