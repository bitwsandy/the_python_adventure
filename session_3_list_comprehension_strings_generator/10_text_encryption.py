# Text Encryption :
#    Create a Python program that takes a string and an encryption key as input
#    and encrypts the string using a simple encryption algorithm.
#    For example, shifting each letter by a certain number of positions
#    in the alphabet.

text = input("Enter a string to encrypt: ")
key = int(input("Enter an encryption key (integer): "))

encrypted_text = ''
# text = "Hello123"
for char in text:
    # hello
    if char.isalpha():
        shift = ord('a') if char.islower() else ord('A')
        encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
        encrypted_text += encrypted_char
        # encrypted_text = encrypted_text + encrypted_char
    else:
        encrypted_text += char

print("Encrypted text:", encrypted_text)
#

key = int(input(("Enter key for decryption : ")))
decrypted_text = ''
# Mjqqt
for char in encrypted_text:
    if char.isalpha():
        shift = ord('a') if char.islower() else ord('A')
        decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
        decrypted_text += decrypted_char
    else:
        decrypted_text += char

print("Decrypted text:", decrypted_text)

# This Python code encrypts and decrypts a string using a Caesar cipher with
# a given encryption key. Here's a brief explanation:
#
# 1. It prompts the user to enter a string to encrypt and an encryption key (an integer).
# 2. It encrypts the input string by shifting each alphabetical character by
#    the encryption key positions.
# 3. It decrypts the encrypted string by shifting each character back by the encryption
#    key positions.
# 4. It prints both the encrypted and decrypted strings.
#


