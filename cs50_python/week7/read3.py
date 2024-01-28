def main():
    names = []

    with open("names.txt", "r") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"hello {name}")

if __name__ == "__main__":
    main()
