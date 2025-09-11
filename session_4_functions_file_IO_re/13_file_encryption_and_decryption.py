# 2. File Encryption and Decryption:
#    Write a Python program that encrypts the content of a text file using a
# simple encryption algorithm (e.g., Caesar cipher) and then decrypts it back to its
# original form.
def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 97 + 3) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + 3) % 26) + 65)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 97 - 3) % 26) + 97) if char.islower() else chr(((ord(char) - 65 - 3) % 26) + 65)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

file_name = r"C:\Users\Sandeep\Desktop\data\wordcount.txt"

# # Encrypt the content of the file
# with open(file_name, "r") as file:
#     content = file.read()
#     encrypted_content = encrypt(content)
#
# # Write the encrypted content back to the file
# with open(file_name, "w") as file:
#     file.write(encrypted_content)

# # Decrypt the content of the file
with open(file_name, "r") as file:
    content = file.read()
    decrypted_content = decrypt(content)

with open(file_name, "w") as file:
    file.write(decrypted_content)
#
# print("Encrypted content:", encrypted_content)
print("Decrypted content:", decrypted_content)



