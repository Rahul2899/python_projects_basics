# Defining function for the calculator
def calculator():
    print("\nWelcome to the world's best calculator!")
    # Writing in a loop for continuing calculations
    while True:
        # Defining variables for input
        num1 = float(input("Enter the first number for calculation: "))
        num2 = float(input("Enter the second number for calculation: "))

        # Menu of calculations
        print("\nChoose options for calculations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # Selecting choice of calculation
        choice = input("\nEnter your choice for calculation (1/2/3/4/5): ")

        # Perform calculations based on the choice
        if choice == '1':
            print("\nYou are performing Addition of numbers:")
            print(f"Results: {num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print("\nYou are performing Subtraction of numbers:")
            print(f"Results: {num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print("\nYou are performing Multiplication of numbers:")
            print(f"Results: {num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 == 0:  # Check for zero divisor
                print("Division can't be performed using zero as the divisor")
            else:
                print("\nYou are performing Division:")
                print(f"Results: {num1} / {num2} = {num1 / num2}")

        elif choice == '5':
            print("Thank you! See you again!")
            break

        else:
            print("Invalid operation choice. Please select a valid option.")

        # Asking if the user wants to continue
        more_calculations = input("\nDo you want to perform another calculation? (Y/N): ")
        if more_calculations.lower() == 'y':
            print("\nEnjoy your calculations!")
        else:
            print("Exiting the calculator. Goodbye!")
            break


# Run the calculator
calculator()
