def main():
    x = int(input("X: "))
    y = int(input("y: "))
    if (x > y):
        print(f"{x} is larger than {y}")
    elif (x < y):
        print(f"{x} is smaller than {y}")
    else:
        print(f"{x} is equal to {y}")

main()
