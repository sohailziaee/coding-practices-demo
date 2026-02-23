"""
Simple Calculator Program
Demonstrates KISS, DRY, and Single Responsibility Principle.
"""

def get_number(prompt):
    """Collects and validates numeric input from the user."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please try again.")


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def display_menu():
    """Displays available calculator operations."""
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


def main():
    """Controls program flow."""
    display_menu()
    choice = input("Select an operation: ")

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }

    if choice in operations:
        try:
            result = operations[choice](num1, num2)
            print(f"Result: {result}")
        except ValueError as error:
            print(error)
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()