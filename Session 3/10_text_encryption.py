# Text Encryption :
#    Create a Python program that takes a string and an encryption key as input
#    and encrypts the string using a simple encryption algorithm.
#    For example, shifting each letter by a certain number of positions
#    in the alphabet.

def encrypt_text(text, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(encrypted_text, key):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

text = input("Enter a string to encrypt: ")
key = int(input("Enter an encryption key (integer): "))
encrypted_text = encrypt_text(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_text(encrypted_text, key)
print("Decrypted text:", decrypted_text)

