from password_generator import PasswordGenerator
def main():
    print("**PASSWORD GENERATOR ***")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
        generator = PasswordGenerator()
        password = generator.generate_password(length)
        print("\nGenerated Password:")
        print(password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()