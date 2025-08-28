# Establish an SSH connection to a remote server and execute a simple command
import paramiko

def ssh_command(ip, port, user, key_file, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # By using AutoAddPolicy, your script will not fail due to unknown host keys;
    # it automatically trusts and stores keys from servers it connects to for the first time.
    # While this is helpful for certain automation tasks
    # (like when connecting to a large number
    # of dynamically managed servers where keys may often change),
    # it comes with a security risk

    try:
        # Using an RSA key instead of a password
        key = paramiko.RSAKey.from_private_key_file(key_file)
        client.connect(ip, port=port, username=user, pkey=key)
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Connection failed. Check IP and Port.")
        return
    except paramiko.ssh_exception.AuthenticationException:
        print("Authentication failed. Check your key or username.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    stdin, stdout, stderr = client.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())
    client.close()


# Example usage
ip = '3.142.73.72'  # or the appropriate IP address
port = 22  # or the appropriate port
user = 'ubuntu' # your username on the server
key_file = r'D:\aws_learning\credentials\tg-demo-server-private.pem'  # e.g., /home/yourname/.ssh/id_rsa
cmd = 'ps'  # Command to execute

ssh_command(ip, port, user, key_file, cmd)
