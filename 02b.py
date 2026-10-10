def write_numbers_to_file(numbers):
    with open("numbers.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

def calculate_average(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            # Calculate the average
            average = sum(numbers) / len(numbers)
            return average
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

    # Write numbers to the file
    write_numbers_to_file(numbers)

    # Calculate the average of numbers in the file
    average = calculate_average("numbers.txt")

    if average is not None:
        print(f"\nThe average of numbers in the file is: {average}")
    else:
        print("\nNo numbers found in the file.")

if __name__ == "__main__":
    main()
