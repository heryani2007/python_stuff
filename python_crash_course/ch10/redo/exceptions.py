def exceptions():
    try:
        a, b = int(input("A: ")), int(input("B "))
        number = a / b
    except ZeroDivisionError:
        print("thou shall not divide by 0")
    else:
        print(number)


exceptions()
