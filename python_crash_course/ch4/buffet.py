def main():
    foods = ("eggs", "bacon", "pancakes", "hash brown")
    print(foods)
    try:
        foods[1] = "sausage"
    except:
        foods = ("eggs", "sausage", "waffle", "hash brown")
        print(foods)


if __name__ == "__main__":
    main()
