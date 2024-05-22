import string
import random

def generate_password(length):
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate and display password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
