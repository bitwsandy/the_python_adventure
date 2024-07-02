import paramiko

def create_ssh_client(ip, port, username, key_file):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=username, pkey=paramiko.RSAKey.from_private_key_file(key_file))
    return client

def multiplexed_operations(client):
    # Channel 1: Command Execution
    stdin, stdout, stderr = client.exec_command('echo "Hello from Channel 1"')
    print("Output from command execution:", stdout.read().decode())

    # Channel 2: File Transfer
    sftp = client.open_sftp()
    sftp.put('01_networking_fundamentals', '/home/ec2-user/demo.txt')
    print("File transfer complete on Channel 2")
    sftp.close()

    # Additional Channel: Another operation can be added here

# Usage
ip = '18.216.86.48'
port = 22  # Standard SSH port
username = 'ec2-user'
key_file = r'D:\aws_learning\credentials\tg-demo-server-private.pem'

client = create_ssh_client(ip, port, username, key_file)
multiplexed_operations(client)
client.close()
