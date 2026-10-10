def write_names_to_file(names):
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

def count_names_in_file(file_path):
    try:
        with open(file_path, "r") as file:
            names = file.readlines()
            return len(names)
    except FileNotFoundError:
        return 0

def main():
    names = []

    while True:
        name = input("Enter a name (or 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        names.append(name)

    write_names_to_file(names)

    count = count_names_in_file("names.txt")

    print(f"\nNumber of names in the file: {count}")

if __name__ == "__main__":
    main()
