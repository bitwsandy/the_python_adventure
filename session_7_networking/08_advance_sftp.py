import paramiko

def sftp_operations():
    # Server details
    ip = 'your_ssh_server_ip'
    port = 22
    username = 'your_username'
    key_file = 'path/to/your/private_key'

    # Connect to the server
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=username, key_filename=key_file)

    # Start an SFTP session
    sftp = client.open_sftp()

    # Create a new directory
    new_directory = '/path/on/server/new_directory'
    try:
        sftp.mkdir(new_directory)
        print(f"Directory created: {new_directory}")
    except IOError as e:
        print(f"Failed to create directory: {e}")

    # List directory contents
    try:
        directory_contents = sftp.listdir('/path/on/server/')
        print("Directory contents:", directory_contents)
    except IOError as e:
        print(f"Failed to list directory contents: {e}")

    # Change file permissions (example: make a file executable)
    file_path = '/path/on/server/file.txt'
    try:
        sftp.chmod(file_path, 0o755)  # Read, write, and execute by owner; read and execute by others
        # This is an octal representation of the file permissions you want to set.
        # In Unix/Linux systems, file permissions are often represented using a
        # three-digit octal number, where each digit can be between 0 and 7.
        # The leading 0o indicates that the number is in octal format.

        print(f"Permissions changed for: {file_path}")
    except IOError as e:
        print(f"Failed to change file permissions: {e}")

    # Close the SFTP session and SSH client
    sftp.close()
    client.close()


if __name__ == '__main__':
    sftp_operations()
