import json
number = [2,3,5,7,11,13]
with open("numbers.json","w") as file_object:
	json.dump(number,file_object)
