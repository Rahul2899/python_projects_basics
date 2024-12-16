# Creating temperature converter using functions

# Creating display function which would print the message
def Display():
    print("\nTell us your choice of actions: ")
    print("1. Convert temperature from Celsius to Fahrenheit")
    print("2. Convert temperature from Fahrenheit to Celsius")
    print("3. Exit")

# Function for temperature conversion
def Cel_Fah(temp):
    return temp * (9 / 5) + 32

def Fah_Cel(temp):
    return (temp - 32) * (5 / 9)

# Defining the main function
def main():
    print("\nWelcome to the Temperature Converter!")

    # Writing loop for continuation
    while True:
        Display()
        try:
            t = int(input("\nEnter your choice for using the temperature converter (1/2/3): "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            continue

        # Conditional statements
        if t == 1:
            temp = float(input("Enter the temperature in Celsius to convert: "))
            print("\nThe converted temperature from Celsius to Fahrenheit is:", Cel_Fah(temp), "F")

        elif t == 2:
            temp = float(input("Enter the temperature in Fahrenheit to convert: "))
            print("\nThe converted temperature from Fahrenheit to Celsius is:", Fah_Cel(temp), "C")

        elif t == 3:
            print("\nThank you! See you again.")
            break

        else:
            print("Invalid choice. Please select a correct option.")
            continue

        # Asking user to continue, with validation loop for valid yes/no input
        while True:
            choice = input("Do you want to continue doing conversions (yes/no)? ").strip().lower()
            
            # Exit the inner loop and continue the main loop
            if choice == 'yes':
                break  
            
            # Exit the main function, thus stopping the program
            elif choice == 'no':
                print("\nThank you for using our converter. Goodbye!")
                return  
            # Stay in the inner loop and ask again
            else:
                print("Invalid choice. Please answer 'yes' or 'no'.")
                continue  

# Calling the function
if __name__ == "__main__":
    main()
