import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    while data is not None:
        print(data.decode())
        if 'Game over' in data.decode():
            s.close()
            break
        if 'Your move' in data.decode():
            play = input("Jogada: ")
            s.sendall(play.encode())
        data = s.recv(1024)
