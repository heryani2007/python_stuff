def main():
    students = [
        {"name" : "Hermione", "house" : "Gryffindor"},
        {"name" : "Harry", "house" : "Gryffindor"},
        {"name" : "Ron", "house" : "Gryffindor"},
        {"name" : "Draco", "house" : "Slytherin"},
        {"name" : "Padma", "house" : "Ravenclaw"}
    ]

    houses = []
    for student in students:
        if student["house"] not in houses:
            houses.append(student["house"])

    print(sorted(houses))
    print(sorted(houses))
if __name__  == "__main__":
    main()
