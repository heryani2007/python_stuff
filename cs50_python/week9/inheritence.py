class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

        ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    def __str__(self):
        return f"{student.name}, {student.house}"
        ...

class Proffessor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{professor.name}, {professor.subject}"

        ...

student = Student("Harry", "Gryffindor")
professor = Proffessor("Severus", "DoJ")

print (student)
print (professor)
