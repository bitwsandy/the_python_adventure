# Paramiko is more commonly used for client-side operations in Python scripts. Paramiko
# does include an SSH server component, but it's not as full-featured or robust as
# dedicated SSH server software like OpenSSH.

# Enable the OpenSSH Server:
#   - Open Settings → Apps → Optional Features.
#   - Scroll down to Add a feature, find OpenSSH Server, and click Install.
#   - Once installed, you might need to manually start the service by going to the
#     Services app, finding OpenSSH SSH Server, and starting it.

# Configure SSH Server Settings (if needed):
#   - The SSH configuration file on Windows is typically located at C:\ProgramData\ssh\sshd_config.
#   - You can edit this file similar to Linux, though default settings are usually sufficient for testing.

# Check the Firewall:
#   - Ensure that the firewall allows inbound connections to port 22 (the default SSH port).