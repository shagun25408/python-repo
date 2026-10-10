def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"File content: {content}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except PermissionError:
        print(f"Error: Permission denied to access {file_path}")
    except IsADirectoryError:
        print(f"Error: {file_path} is a directory, not a file")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file at {file_path}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

def main():
    file_path = input("Enter the file path: ")
    read_file(file_path)

if __name__ == "__main__":
    main()

