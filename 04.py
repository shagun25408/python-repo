def perform_integer_division(a, b):
    try:
        result = a // b
        print(result)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")

def main():
    try:
        n = int(input("Enter the number of test cases: "))
    except ValueError:
        print("Error Code: invalid literal for int() with base 10")

    for _ in range(n):
        try:
            a, b = map(int, input().split())
            perform_integer_division(a, b)
        except ValueError as e:
            print(f"Error Code: {e}")

if __name__ == "__main__":
    main()