import socket
import threading
import paramiko

# Generate host key using Paramiko
host_key = paramiko.RSAKey.generate(bits=2048)

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'testuser') and (password == 'testpassword'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

def handle_client(client_socket):
    transport = paramiko.Transport(client_socket)
    transport.add_server_key(host_key)

    server = Server()
    try:
        transport.start_server(server=server)
    except paramiko.SSHException:
        print('SSH session startup failed')

    channel = transport.accept(20)
    if channel is None:
        print('No channel.')
        transport.close()
        return

    print('Authenticated!')
    channel.send('Welcome to the SSH server!')
    while True:
        command = channel.recv(1024).decode('utf-8')
        if not command:
            continue
        if command == 'exit':
            channel.send('Exiting...\n')
            break
        # Example command handling
        elif command.strip() == 'date':
            channel.send('The date is now!\n')
        else:
            channel.send('Command received: {}\n'.format(command))
    channel.close()
    transport.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.socket():
    #       This creates a new socket object.
    #       A socket is an endpoint for sending or receiving data across a computer
    #       network.

    # socket.AF_INET:
    #       This specifies the address family for the socket.
    #       AF_INET stands for Address Family Internet, which means the socket will
    #       use IPv4 addresses.
    #       It indicates that the socket is intended to be used for network
    #       communication using the Internet Protocol version 4.

    # socket.SOCK_STREAM:
    #       This specifies the socket type.
    #       SOCK_STREAM indicates that the socket will be a stream socket,
    #       which provides sequenced, reliable, two-way, connection-based byte streams.
    #       This is the type of socket used for TCP (Transmission Control Protocol)
    #       connections, which are used in SSH (Secure Shell) connections.

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # server_socket.setsockopt: This method is used to set a socket option.

    # socket.SOL_SOCKET:
    #       This specifies the level at which the option is defined.
    #       SOL_SOCKET refers to socket-level options.

    # socket.SO_REUSEADDR:
    #       This specifies the option name.
    #       SO_REUSEADDR is a socket option that allows a socket to bind to an address
    #       that is already in use. It is useful in scenarios where you want to
    #       quickly restart a server that was previously bound to a specific port
    #       without waiting for the socket to be fully closed and released by the
    #       operating system.
    # By setting the SO_REUSEADDR option, you allow the socket to be reused, which is
    # particularly useful in the following situations:
    # Server Restart:
    #       When you stop and restart a server, the port it was using might still be
    #       considered "in use" by the operating system. Setting this option allows
    #       the server to rebind to the same port immediately.
    # Multiple Instances:
    #       In some cases, you might have multiple instances of an application that
    #       need to bind to the same port (e.g., multicast applications).

    # 1: This is the value for the option. Setting this to 1 enables the SO_REUSEADDR option.

    server_socket.bind(('0.0.0.0', 2200))  # Bind to all interfaces on port 2200
    server_socket.listen(100)
    print('Listening for connection ...')
    while True:
        client, addr = server_socket.accept()
        print('Got a connection from ', addr)
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

start_server()
