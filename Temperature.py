# Welcome message
print("Welcome to the Temperature Converter")

while True:
    # Display options to the user
    print("\nTell us your form of temperature conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    # Input prompt
    t = input("Select the option you want to perform (1/2/3): ")

    # Check conditions
    if t == '1':
        temp = float(input("Enter the temperature in Celsius: "))
        print("The temperature in Fahrenheit is:", temp * (9 / 5) + 32, "F")

    elif t == '2':
        temp = float(input("Enter the temperature in Fahrenheit: "))
        print("The temperature in Celsius is:", (temp - 32) * (5 / 9), "C")

    
    # Exit the loop if the user selects option 3
    elif t == '3':
        print("Thank you. See you again!")
        break  

    
    # Restart the loop for invalid input
    else:
        print("Invalid choice. Please select a valid option.")
        continue  

    # Ask the user if they want to continue
    choice = input("Do you want to continue another conversion (yes/no)? ").strip().lower()
    
    # Exit the loop if the user chooses not to continue
    if choice != 'yes':
        print("Thank you for using our converter. Goodbye!")
        break  
