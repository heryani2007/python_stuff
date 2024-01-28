#List
def main():
    students = [
        {"name" : "Hermione", "house" : "Gryffindor"},
        {"name" : "Harry", "house" : "Gryffindor"},
        {"name" : "Ron", "house" : "Gryffindor"},
        {"name" : "Draco", "house" : "Slytherin"},
        {"name" : "Padma", "house" : "Ravenclaw"}
    ]

    houses = list()
    for student in students:
        houses.append(student["house"])

    print(sorted(houses))
if __name__  == "__main__":
    main()

# Set
def main():
    students = [
        {"name" : "Hermione", "house" : "Gryffindor"},
        {"name" : "Harry", "house" : "Gryffindor"},
        {"name" : "Ron", "house" : "Gryffindor"},
        {"name" : "Draco", "house" : "Slytherin"},
        {"name" : "Padma", "house" : "Ravenclaw"}
    ]

    houses = set()
    for student in students:
        houses.add(student["house"])

    print(sorted(houses))
if __name__  == "__main__":
    main()
