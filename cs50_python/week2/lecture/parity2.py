def main():
    x = int(input("X: "))
    if (is_true(x) is True):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")


def is_true(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
