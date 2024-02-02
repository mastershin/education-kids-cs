import socket
import threading
import sys

def handle_client(client_socket):
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            break
        print("\nReceived:", msg.decode())

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen(1)
    print(f"Server listening on port {port}")

    client_sock, addr = server.accept()
    print(f"Connection from {addr} has been established.")

    client_handler = threading.Thread(target=handle_client, args=(client_sock,))
    client_handler.start()

    while True:
        msg = input("You: ")
        client_sock.send(msg.encode())

def start_client(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    server_handler = threading.Thread(target=handle_client, args=(client,))
    server_handler.start()

    while True:
        msg = input("You: ")
        client.send(msg.encode())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python chat.py server <Port> or python chat.py client <Server IP> <Port>")
        sys.exit(1)

    if sys.argv[1] == "server":
        start_server(int(sys.argv[2]))
    elif sys.argv[1] == "client":
        start_client(sys.argv[2], int(sys.argv[3]))

