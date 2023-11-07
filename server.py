from board import Board
from player import Player
import time
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    board = Board()
    connection = s.accept()
    player1 = Player(connection[0], connection[1], 'white')
    print(f"Player 1 Connected by {player1.address}")
    connection = s.accept()
    player2 = Player(connection[0], connection[1], 'black')
    print(f"Player 2 Connected by {player1.address}")

    while True:
        if board.toPlay == 'white':
            playing = player1
            waiting = player2
        else:
            playing = player2
            waiting = player1
        print(board.toPlay + " to play")


        try:
            if playing.timeout():
                waiting.socket.sendall(
                    (player2.getTime() + board.unicodeBoard() + player1.getTime() +
                     board.toPlay + "'s time ran out, you win! Game over").encode())
            elif board.kingCaptured(playing.color):
                waiting.socket.sendall(
                    (player2.getTime() + board.unicodeBoard() + player1.getTime() +
                     board.toPlay + "'s king got captured, you win! Game over").encode())
            else:
                waiting.socket.sendall(
                    (player2.getTime() + board.unicodeBoard() + player1.getTime() +
                     "Waiting for opponent - " + board.toPlay + " to play").encode())
        except WindowsError:
            connection = s.accept()
            if board.toPlay == 'white':
                player2.updateConnection(connection[0], connection[1])
            else:
                player1.updateConnection(connection[0], connection[1])

        try:
            if playing.timeout():
                playing.socket.sendall(
                    (player2.getTime() + board.unicodeBoard() + player1.getTime() +
                     board.toPlay + "'s time ran out, you lose! Game over").encode())
                s.close()
                break
            elif board.kingCaptured(playing.color):
                playing.socket.sendall(
                    (player2.getTime() + board.unicodeBoard() + player1.getTime() +
                     board.toPlay + "'s king got captured, you win! Game over").encode())
            else:
                playing.socket.sendall(
                    (player2.getTime() + board.unicodeBoard() + player1.getTime() +
                     "Your move - " + board.toPlay + " to play").encode())
            start = time.perf_counter()
            data = playing.socket.recv(1024)
            data = data.decode().split(' ')
            print(data)
            if len(data) == 2:
                print('Jogada OK')
                print('Jogada: ', board.play(data[0], data[1]))
            playing.incrementTime(time.perf_counter() - start)
        except WindowsError:
            connection = s.accept()
            if board.toPlay == 'white':
                player1.updateConnection(connection[0], connection[1])
            else:
                player2.updateConnection(connection[0], connection[1])
