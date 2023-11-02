from board import Board

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    board = Board()
    player1, addr = s.accept()
    print(f"Player 1 Connected by {addr}")
    player2, addr2 = s.accept()
    print(f"Player 2 Connected by {addr2}")

    while True:
        if board.toPlay == 'white':
            playing = player1
            waiting = player2
        else:
            playing = player2
            waiting = player1
        print(board.toPlay + " to play")

        try:
            waiting.sendall((board.unicodeBoard() + "\n Waiting for opponent - " + board.toPlay + " to play").encode())
        except WindowsError:
            if board.toPlay == 'white':
                player2, addr = s.accept()
            else:
                player1, addr = s.accept()

        try:
            playing.sendall((board.unicodeBoard() + "\n Your move - " + board.toPlay + " to play").encode())
            data = playing.recv(1024)
            data = data.decode().split(' ')
            print(data)
            if len(data) == 2:
                print('Jogada OK')
                print('Jogada: ', board.play(data[0], data[1]))
        except WindowsError:
            if board.toPlay == 'white':
                player1, addr = s.accept()
            else:
                player2, addr = s.accept()