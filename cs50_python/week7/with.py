def main():
    while True:
        name = input("name: ")

        with open("names2.txt","w") as file:
            if name == "close":
                file.close
                break
            else:
                file.write(f"{name}\n")

if __name__ == "__main__":
    main()
