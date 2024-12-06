def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def calculator():
    print("\nWelcome to the Simple Calculator App!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    print("7. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "7":
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "1":
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == "5":
            print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
        elif choice == "6":
            print(f"Result: {num1} ^ {num2} = {exponent(num1, num2)}")

if __name__ == "__main__":
    calculator()
