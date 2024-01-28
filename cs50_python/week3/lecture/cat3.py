def main():
    while True:
        try:
            n = int(input("n: "))
            if n < 0:
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    for _ in range(n):
        print("meow")

main()
