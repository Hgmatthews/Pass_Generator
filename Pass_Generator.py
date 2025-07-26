import sys
import random
import string
#imported functions

class PasswordManager:
    def __init__(self):
        self.passwords = {}
    # Shift value for Caesar Cipher
       
        self.shift = 3 
        self.load_passwords()  

    # Load passwords from file when the program starts
   
    def display_menu(self):
    # Display the main menu options
        
        print("\nWelcome to Password Manager!")
        
        print("\n1. Add New Password")
        print("2. View Passwords")
        print("3. Remove Password")
        print("4. Generate Strong Password")
        print("5. Exit")
        choice = input("\nEnter your choice: ")
        return choice

    # Caesar Cipher encryption method
    def caesar_cipher_encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted_char = chr((ord(char) + self.shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) + self.shift - 97) % 26 + 97)
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        return encrypted_text

    # Caesar Cipher decryption method
    def caesar_cipher_decrypt(self, text):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted_char = chr((ord(char) - self.shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) - self.shift - 97) % 26 + 97)
                decrypted_text += shifted_char
            else:
                decrypted_text += char
        return decrypted_text

    # Load passwords from file
    def load_passwords(self):
        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    service, encrypted_password = line.strip().split(":")
                    self.passwords[service] = encrypted_password
        except FileNotFoundError:
            pass 
    # If the file doesn't exist, ignore it

    # Save passwords to file
    def save_passwords(self):
        with open("passwords.txt", "w") as file:
            for service, encrypted_password in self.passwords.items():
                file.write(f"{service}:{encrypted_password}\n")

    # Add a new password
    def add_password(self):
        service = input("What will this password be used for?: ")
        while True:
            password = input("Enter the password: ")

    # Check password criteria
            missing_characters = []
            if len(password) < 8:
                missing_characters.append("at least 8 characters")
            if not any(char.isupper() for char in password):
                missing_characters.append("at least one uppercase letter")
            if not any(char.islower() for char in password):
                missing_characters.append("at least one lowercase letter")
            if not any(char.isdigit() for char in password):
                missing_characters.append("at least one digit")
            if any(char in ['$','#','_','-','+','='] for char in password):
                missing_characters.append("no special characters like $, #, _, -, +, =")
            if missing_characters:
                print("Password does not meet the requirements. It is missing:")
                for criteria in missing_characters:
                    print(criteria)
                print("Please enter a new password.")
            else:
    # Encrypt password using Caesar Cipher
                encrypted_password = self.caesar_cipher_encrypt(password)
                self.passwords[service] = encrypted_password
                self.save_passwords()  
    # Save passwords to file after adding a new one
               
                print("\nPassword added successfully!")
                break

    # View saved passwords
    
    def view_passwords(self):
        if not self.passwords:
            print("No passwords saved yet!")
            return
        print("Your saved passwords:")
        for service, encrypted_password in self.passwords.items():
            decrypted_password = self.caesar_cipher_decrypt(encrypted_password)
            print(f"Service: {service}, Password: {decrypted_password}")

   
     # Remove a password
    
    def remove_password(self):
        service = input("Enter the service name to remove its password: ")
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()  
    # Save passwords to file after removing one
           
            print("Password removed successfully!")
        else:
            print("Service not found!")

    # Generate a strong password
    
    def generate_strong_password(self):
        length = int(input("Enter the length of the password *cannot be less than 8 characters!: "))
        chars = string.ascii_letters + string.digits + '!@%^&*()'
        password = ''.join(random.choice(chars) for _ in range(length))

        missing_characters = []
        if length < 8:
            missing_characters.append("at least 8 characters")
        if not any(char.isupper() for char in password):
            missing_characters.append("at least one uppercase letter")
        if not any(char.islower() for char in password):
            missing_characters.append("at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            missing_characters.append("at least one digit")
        if any(char in ['$','#','_','-','+','='] for char in password):
            missing_characters.append("no special characters like $, #, _, -, +, =")
        if missing_characters:
            print("Generated password is not strong enough. It is missing:")
            for criteria in missing_characters:
                print(criteria)
            print("Please generate a new password.")
        else:
            print("Generated Strong Password:", password)
            save_option = input("Do you want to save this password? (yes/no): ")
            if save_option.lower() == "yes":
                service = input("Enter the service name to save this password: ")
                encrypted_password = self.caesar_cipher_encrypt(password)
                self.passwords[service] = encrypted_password
                self.save_passwords()  
    # Save passwords to file
                print("Password saved successfully!")

   
    # Main method to run the password manager
    
    def run(self):
        while True:
            choice = self.display_menu()
            if choice == "1":
                self.add_password()
            elif choice == "2":
                self.view_passwords()
            elif choice == "3":
                self.remove_password()
            elif choice == "4":
                self.generate_strong_password()
            elif choice == "5":
                print("Exiting Password Manager. Goodbye!")
                self.save_passwords()  
    # Save passwords to file before exiting
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = PasswordManager()
    manager.run()
