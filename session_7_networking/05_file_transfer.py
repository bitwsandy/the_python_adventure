#  This exercise will involve setting up an SFTP session for file transfer,
#  which is a common use case for Paramiko in real-world applications. It will provide a
#  practical understanding of handling files securely over SSH.

import paramiko

def setup_sftp_session(ip, port, user, key_file):
    transport = paramiko.Transport((ip, port))
    key = paramiko.RSAKey.from_private_key_file(key_file)
    transport.connect(username=user, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(transport)
    return sftp

def upload_file(sftp, local_path, remote_path):
    sftp.put(local_path, remote_path)
    print(f"Uploaded {local_path} to {remote_path}")

def download_file(sftp, remote_path, local_path):
    sftp.get(remote_path, local_path)
    print(f"Downloaded {remote_path} to {local_path}")

# Example usage
ip = '18.223.164.180'  # or the appropriate IP address
port = 22  # or the appropriate port
user = 'ec2-user' # your username on the server
key_file = r'D:\aws_learning\credentials\tg-demo-server-private.pem'  # e.g., /home/yourname/.ssh/id_rsa


# Establish SFTP Session
sftp = setup_sftp_session(ip, port, user, key_file)

# Specify file paths
local_upload_path = r'C:\Users\Sandeep\Desktop\data\cr.txt'
remote_upload_path = r'/home/ec2-user/sample/cr_uploaded.txt'

local_download_path = r'C:\Users\Sandeep\Desktop\data\cr_downloaded.txt'
remote_download_path = r'/home/ec2-user/sample/cr_uploaded.txt'

# Upload and download files
upload_file(sftp, local_upload_path, remote_upload_path)
download_file(sftp, remote_download_path, local_download_path)

# Close the SFTP session
sftp.close()
