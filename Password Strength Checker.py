# Password Strength Checker

# Function to check password strength
def check_password(password):
    
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    # Strong password condition
    if length and has_upper and has_lower and has_digit and has_special:
        return "Strong Password 💪"
    
    # Medium password condition
    elif length and ((has_upper and has_lower) or (has_digit and has_special)):
        return "Medium Password 🙂"
    
    else:
        return "Weak Password ❌"


# Main Program
def main():
    while True:
        password = input("Enter your password: ")
        result = check_password(password)
        print("Password Strength:", result)

        choice = input("Check another password? (yes/no): ")
        if choice.lower() != "yes":
            print("Program Ended.")
            break


# Run program
if __name__ == "__main__":
    main()