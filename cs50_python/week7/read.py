def main():

    with open("names.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line,end="")

if __name__ == "__main__":
    main()
