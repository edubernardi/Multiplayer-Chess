from board import Board

board = Board()
print(board.unicodeBoard())
board.play("A2", "A4")
board.play("A7", "A5")
print(board.unicodeBoard())
board.play("A1", "A3")
board.play("B7", "B5")
board.play("A3", "H3")
board.play("C7", "C5")
board.play("D2", "D3")
board.play("D7", "D5")
board.play("H3", "H5")
board.play("D5", "D4")
board.play("H5", "C5")
board.play("E7", "E5")
print(board.unicodeBoard())
board.play("C5", "C8")
board.play("F8", "A3")
board.play("C1", "H6")
board.play("A3", "B2")
board.play("H6", "G7")
board.play("B8", "D7")
board.play("D1", "D2")
board.play("D8", "B6")
board.play("E1", "D1")
print(board.unicodeBoard())
