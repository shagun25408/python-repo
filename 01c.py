def write_names_to_file(names):
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

def find_longest_name(file_path):
    try:
        with open(file_path, "r") as file:
            names = file.readlines()
            longest_name = max(name.strip() for name in names)
            return longest_name
    except FileNotFoundError:
        return None

def main():
    names = []

    while True:
        name = input("Enter a name (or 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        names.append(name)

    
    write_names_to_file(names)

    longest_name = find_longest_name("names.txt")

    if longest_name:
        print(f"\nThe longest name in the file is: {longest_name}")
    else:
        print("\nNo names found in the file.")

if __name__ == "__main__":
    main()
