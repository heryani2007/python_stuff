def main():

    with open("names.txt", "r") as file:
        for line in file:
            print(line,end="")

if __name__ == "__main__":
    main()
