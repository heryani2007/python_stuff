def main():
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append(f"{name} is in {house}")
        print(sorted(students))

if __name__ == "__main__":
    main()
