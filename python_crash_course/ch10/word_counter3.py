def counter():
    files = [
        "./books/alice.txt",
        "./books/moby.txt",
        "./books/1984.txt",
        "./books/yan.txt",
    ]
    for file in files:
        try:
            with open(file) as file_object:
                words = file_object.read().split()
                words = len(words)
        except FileNotFoundError:
            pass
        else:
            print(words)


if __name__ == "__main__":
    counter()
