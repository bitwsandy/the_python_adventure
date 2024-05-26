text = input("Enter a string to encrypt: ")
key = int(input("Enter an encryption key (integer): "))

encrypted_text = ''
for char in text:
    # hello
    if char.isalpha():
        shift = ord('a') if char.islower() else ord('A')
        encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
        encrypted_text += encrypted_char
    else:
        encrypted_text += char

print("Encrypted text:", encrypted_text)

key = int(input("Enter a key to decrypt : "))
decrypted_text = ''
for char in encrypted_text:
    if char.isalpha():
        shift = ord('a') if char.islower() else ord('A')
        decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
        decrypted_text += decrypted_char
    else:
        decrypted_text += char

print("Decrypted text:", decrypted_text)
