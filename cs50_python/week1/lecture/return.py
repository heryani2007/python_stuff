def main():
    x = int(input("X: "))
    print(square(x))

def square(x):
    if isinstance(x, int):
        return x * x
    else:
        return "Plase input number"

main()
