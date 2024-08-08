# Managing multiple SSH connections and channels using Paramiko
# This scenario is common in network automation, where tasks need to be executed
# on multiple servers at the same time.

import paramiko
import threading

def ssh_session(ip, port, user, key_file, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, pkey=paramiko.RSAKey.from_private_key_file(key_file))
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    client.close()


def handle_multiple_ssh_sessions(commands_per_server):
    threads = []
    for server_details, command in commands_per_server:
        ip, port, user, key_file = server_details
        th = threading.Thread(target=ssh_session, args=(ip, port, user, key_file, command))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()  # Wait for all threads to complete


# Example usage
commands_per_server = [
    (('18.223.164.180', 22, 'ec2-user', r'D:\aws_learning\credentials\tg-demo-server-private.pem'), 'uptime'),
    (('3.144.162.58', 22, 'ec2-user', r'D:\aws_learning\credentials\tg-demo-server-private.pem'), 'df -h'),
    (('18.221.247.193', 22, 'ec2-user', r'D:\aws_learning\credentials\tg-demo-server-private.pem'), 'whoami')
]

handle_multiple_ssh_sessions(commands_per_server)
