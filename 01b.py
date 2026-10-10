def write_names_to_file(names):
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

def count_names_starting_with_vowel(file_path):
    vowels = set("aeiouAEIOU")
    count = 0

    try:
        with open(file_path, "r") as file:
            names = file.readlines()
            for name in names:
                if name.strip() and name[0] in vowels:
                    count += 1
        return count
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

    count = count_names_starting_with_vowel("names.txt")

    print(f"\nNumber of names starting with a vowel in the file: {count}")

if __name__ == "__main__":
    main()
