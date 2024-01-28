# Creating a list, a dictionary, and a tuple in Python

# List
my_list = [1, 2, 3, "apple", "banana"]
my_list.append("boomer")
# Dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict2 = (my_dict | {"gen" : "boomer"})

# Tuple
my_tuple = (10, 20, 30, "orange", "grape")
if my_tuple[0] == 10:
    my_tuple[0] = 'doom'

print(my_list, my_dict2, my_tuple)

