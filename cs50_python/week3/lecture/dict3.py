def main():
    students = [
        {"name":"Hermoine", "house":"Gryffindor", "patronus":"otter"},
        {"name":"Harry", "house":"Gryffindor", "patronus":"stag"},
        {"name":"Ron", "house":"Gryffindor", "patronus":"terrier"},
        {"name":"Draco", "house":"Slytherin", "patronus":None}
    ]
    for student in students:
        print(f"{student["name"]} is in house {student["house"]} their patronus is {student["patronus"]}")
main()
