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

def ssh_connect_with_key(ip, port, username, key_filename):
    # Set up the SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect using the private key
    client.connect(hostname=ip, port=port, username=username, key_filename=key_filename)
    print(f"Connected to {ip} using key-based authentication.")

    # Close the connection
    client.close()
    print("Connection closed.")

if __name__ == '__main__':
    key_filename = 'my_ssh_key'
    ip = 'example.com'  # Change to your server's IP
    port = 22
    username = 'access_keys'

    # Generate and save SSH keys
    generate_keys(key_filename)

    # Connect using the generated SSH key
    ssh_connect_with_key(ip, port, username, key_filename)
