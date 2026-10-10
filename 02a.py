def write_numbers_to_file(numbers):
    with open("numbers.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

def find_max_number(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            # Find the maximum number
            max_number = max(numbers)
            return max_number
    except FileNotFoundError:
        return None

def main():
    numbers = []

    # Input integers until the user decides to stop
    while True:
        try:
            number = int(input("Enter an integer (or 'exit' to stop): "))
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break

    
    write_numbers_to_file(numbers)


    max_number = find_max_number("numbers.txt")

    if max_number is not None:
        print(f"\nThe maximum number in the file is: {max_number}")
    else:
        print("\nNo numbers found in the file.")

if __name__ == "__main__":
    main()
