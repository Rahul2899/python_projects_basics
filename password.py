import re
import getpass

def password_strength():
    while True:
        # Input password securely
        inp = getpass.getpass("\nEnter your password: ")

        # Password strength criteria
        length_error = len(inp) < 8
        lower_case_error = not re.search(r'[a-z]', inp)
        upper_case_error = not re.search(r'[A-Z]', inp)
        number_error = not re.search(r'\d', inp)
        symbol_error = not re.search(r'[!@#$%^&*()]', inp)

        # Check for errors
        if length_error or lower_case_error or upper_case_error or number_error or symbol_error:
            print("\nWeak password. Improve it by fixing the following:")

            if length_error:
                print("- Password length should be at least 8 characters.")
            if lower_case_error:
                print("- Add at least one lowercase letter (a-z).")
            if upper_case_error:
                print("- Add at least one uppercase letter (A-Z).")
            if number_error:
                print("- Add at least one number (0-9).")
            if symbol_error:
                print("- Add at least one special character (!, @, #, $, %, ^, &, *, (, )).")

        else:
            print("\nPassword is strong! No one can hack your account.")
            break

# Call the function
password_strength()
