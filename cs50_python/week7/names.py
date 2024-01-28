def main():
    names = []
    count = int(input("List Size: "))

    for _ in range(count):
        name = input("name: ")
        names.append(name)

        print(names)

    for name in sorted(names):
        print(f"hello, {name}")
main()
