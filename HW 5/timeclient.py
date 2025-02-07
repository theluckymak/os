import socket
import sys


def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    message = client_socket.recv(1024).decode()

    print(f"Received from server: {message}")

    client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 timeclient.py <server_ip> <port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    start_client(server_ip, server_port)
