class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return "a student"

    #Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Terrier":
                return "🐶"
            case _:
                return "/"


def main():
    student = get_student()
    #student.house = "Playboy"
    print(f"{student.name} from {student.house}")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)
    return student


if __name__ == "__main__":
    main()

