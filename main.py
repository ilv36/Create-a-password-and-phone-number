import random
import string
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def create_passwords(num_passwords):
    passwords = []
    for _ in range(num_passwords):
        length = random.randint(5, 10)
        passwords.append(generate_password(length))
    return passwords

def save_passwords(passwords, base_filename="password.txt"):
    filename = base_filename
    if os.path.exists(filename):
        base, ext = os.path.splitext(base_filename)
        counter = 1
        while os.path.exists(filename):
            filename = f"{base}({counter}){ext}"
            counter += 1
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(password + '\n')
    print(f"\nPasswords saved to {filename}\n")

def generate_phone_number():
    return '0' + ''.join(random.choice(string.digits) for _ in range(9))

def create_phone_numbers(num_phone_numbers):
    phone_numbers = []
    for _ in range(num_phone_numbers):
        phone_numbers.append(generate_phone_number())
    return phone_numbers

def save_phone_numbers(phone_numbers, base_filename="phone.txt"):
    filename = base_filename
    if os.path.exists(filename):
        base, ext = os.path.splitext(base_filename)
        counter = 1
        while os.path.exists(filename):
            filename = f"{base}({counter}){ext}"
            counter += 1
    with open(filename, 'w') as f:
        for phone_number in phone_numbers:
            f.write(phone_number + '\n')
    print(f"\nPhone numbers saved to {filename}\n")

def main():
    print("========================================")
    print("          Generator")
    print("========================================")
    print("1. Generate Passwords")
    print("2. Generate Phone Numbers")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        num_passwords = int(input("\nEnter the number of passwords you want to generate: "))
        passwords = create_passwords(num_passwords)
        
        # Display the generated passwords in cmd
        print("\nGenerated Passwords:")
        print("========================================")
        for idx, password in enumerate(passwords, 1):
            print(f"{idx}: {password}")
        print("========================================")
        
        save_passwords(passwords)
    
    elif choice == '2':
        num_phone_numbers = int(input("\nEnter the number of phone numbers you want to generate: "))
        phone_numbers = create_phone_numbers(num_phone_numbers)
        
        # Display the generated phone numbers in cmd
        print("\nGenerated Phone Numbers:")
        print("========================================")
        for idx, phone_number in enumerate(phone_numbers, 1):
            print(f"{idx}: {phone_number}")
        print("========================================")
        
        save_phone_numbers(phone_numbers)
    
    else:
        print("Invalid choice. Please enter 1 or 2.")
    
    input("Press any key to exit...")

if __name__ == "__main__":
    main()
