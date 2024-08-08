from cryptography.fernet import Fernet

def generate_key():
    # Generate a key and save it into a file
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    # Load the previously generated key
    return open("secret.key", "rb").read()

def encrypt_message(message, key):
    # Encrypt the message
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Decrypt the message
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == '__main__':
    key = generate_key()  # Generate and save the key
    key = load_key()  # Load the encryption key

    # Define a message
    original_message = "This is a secret message"
    print("Original:", original_message)

    # Encrypt the message
    encrypted = encrypt_message(original_message, key)
    print("Encrypted:", encrypted)

    # Decrypt the message
    decrypted = decrypt_message(encrypted, key)
    print("Decrypted:", decrypted)
