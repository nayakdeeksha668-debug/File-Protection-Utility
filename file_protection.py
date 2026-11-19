

from cryptography.fernet import Fernet, InvalidToken
import os

# Generate or load secret key
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as file:
        file.write(key)
else:
    with open("secret.key", "rb") as file:
        key = file.read()

fernet = Fernet(key)


# Function to encrypt a file
def encrypt_file():
    filename = input("Enter file name to encrypt: ")

    if not os.path.isfile(filename):
        print("File not found!")
        return

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")


# Function to decrypt a file
def decrypt_file():
    filename = input("Enter encrypted file name: ")

    if not os.path.isfile(filename):
        print("File not found!")
        return

    try:
        with open(filename, "rb") as file:
            data = file.read()

        decrypted_data = fernet.decrypt(data)

        output_name = "restored_" + os.path.basename(filename)

        if output_name.endswith(".encrypted"):
            output_name = output_name[:-10]

        with open(output_name, "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")
        print("Restored file:", output_name)

    except InvalidToken:
        print("Wrong key or invalid encrypted file!")


# Main menu
while True:
    print("\n================================")
    print("     FILE PROTECTION UTILITY")
    print("================================")
    print("1. Encrypt a File")
    print("2. Decrypt a File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        encrypt_file()

    elif choice == "2":
        decrypt_file()

    elif choice == "3":
        print("Thank you for using File Protection Utility!")
        break

    else:
        print("Invalid choice! Please try again.")
