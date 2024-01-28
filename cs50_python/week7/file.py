def main():
    while True:
        uname = input("name: ")

        fname = open("names.txt", "a")
        fname.write(f" {uname}\n")
        fname.close

main()
