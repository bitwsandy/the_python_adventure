import paramiko
def generate_keys(key_filename):
    # Generate a new private key
    private_key = paramiko.RSAKey.generate(bits=2048)

    # Save the private key
    private_key.write_private_key_file(f"{key_filename}")

    # Create and save the public key
    public_key = f"{private_key.get_name()} {private_key.get_base64()}"
    with open(f"{key_filename}.pub", 'w') as pub_file:
        pub_file.write(public_key)
    print("SSH key pair generated and saved.")

generate_keys('keys/id')