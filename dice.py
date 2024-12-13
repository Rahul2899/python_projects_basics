

inp ='y'


while(inp=='y' or inp=='Y')


def calculator():
    print("Let's calculate!")

    # Input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Input operation choice
    choice = input("\nEnter the number corresponding to your choice (1/2/3/4): ")

    # Perform calculation and display result
    print("\nResult:")
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please restart the program.")

# Run the calculator function
calculator()