def main():
    names_list = []
    print(f"This is the list {names_list}")


    while True:
        new_name = input("Append to list: ")
        names_list.append(new_name)

        # Write the new name to the file
        with open("names.txt", "a") as file:
            file.write(new_name + "\n")

        print(f"This is the appended list {names_list}")

if __name__ == "__main__":
    main()
