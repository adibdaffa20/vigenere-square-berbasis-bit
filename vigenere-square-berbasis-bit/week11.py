def vigenere_cipher(message, key, operation):
    result = ""
    key_length = len(key)

    for i in range(len(message)):
        message_char = ord(message[i])
        key_char = ord(key[i % key_length])

        if operation == 1:  # Encryption
            result_char = message_char ^ key_char
        elif operation == 2:  # Decryption
            result_char = message_char ^ key_char
        else:
            raise ValueError("Invalid operation. Use 1 for encryption or 2 for decryption.")

        result += chr(result_char)

    return result

def main():
    print("Vigenere Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice not in [1, 2]:
        print("Invalid choice. Exiting.")
        return

    message = input("Enter the message: ")
    key = input("Enter the key: ")

    if choice == 1:
        result = vigenere_cipher(message, key, 1)
        print("Encrypted Message:", result)
    elif choice == 2:
        result = vigenere_cipher(message, key, 2)
        print("Decrypted Message:", result)

if __name__ == "__main__":
    main()
