# practice match (switch) statements

def main():
    name = input("name ")
    match name:
        case "Harry" | "Hermoine" | "Ron":
            print("Gryfindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("who?")

main()
