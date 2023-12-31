from piece import *


class Board():

    def __init__(self):
        board = [Rook('black', 8, 1), Knight('black', 8, 2), Bishop('black', 8, 3),
                 Queen('black', 8, 4), King('black', 8, 5), Bishop('black', 8, 6),
                 Knight('black', 8, 7), Rook('black', 8, 8)]

        for i in range(1, 9):
            board.append(Pawn('black', 7, i))

        board += [None] * 32

        for i in range(1, 9):
            board.append(Pawn('white', 2, i))

        board += [Rook('white', 1, 1), Knight('white', 1, 2), Bishop('white', 1, 3),
                  Queen('white', 1, 4), King('white', 1, 5), Bishop('white', 1, 6),
                  Knight('white', 1, 7), Rook('white', 1, 8)]

        self.board = board
        self.toPlay = 'white'

    def unicodeBoard(self):
        unicodeBoard = "8  "
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i * 8 + j] is None:
                    unicodeBoard += "_   "
                else:
                    unicodeBoard += self.board[i * 8 + j].toString() + "   "
            unicodeBoard += "\n"
            if i < 7:
                unicodeBoard += str(7 - i) + "  "
                i -= 1
            else:
                unicodeBoard += "   A   B   C   D   E   F   G   H\n"
        return unicodeBoard

    def play(self, origin, destination):
        if len(origin) != 2 or len(destination) != 2:
            return False

        column = ord(destination[0]) - 64
        row = int(destination[1])

        if column not in range(1, 9) or row not in range(1, 9):
            return False

        piece = self.board[ord(origin[0]) - 65 + (8 - int(origin[1])) * 8]
        destinationPiece = self.board[ord(destination[0]) - 65 + (8 - int(destination[1])) * 8]

        if piece is None:
            return False

        if piece.color != self.toPlay:
            return False

        if piece.validate(destinationPiece, row, column, self):
            self.board[column + 7 + ((7 - row) * 8)] = piece
            self.board[ord(origin[0]) - 65 + (8 - int(origin[1])) * 8] = None

            piece.column = column
            piece.row = row

            self.toPlay = 'black' if self.toPlay == 'white' else 'white'
            return True
        return False

    def clearPathLine(self, column, destinationColumn, row, destinationRow):
        if column == destinationColumn:
            step = 1 if row < destinationRow else - 1
            for i in range(row + step, destinationRow, step):
                if self.board[column + 7 + ((7 - i) * 8)] is not None:
                    return False
        if row == destinationRow:
            step = 1 if row < destinationRow else - 1
            for i in range(column + step, destinationColumn, step):
                if self.board[i + 7 + ((7 - row) * 8)] is not None:
                    return False
        return True

    def clearPathDiagonal(self, column, destinationColumn, row, destinationRow):
        verticalStep = 1 if row < destinationRow else - 1
        horizontalStep = 1 if column < destinationColumn else - 1
        for i in range(1, abs(row - destinationRow)):
            column += horizontalStep
            row += verticalStep
            if self.board[column + 7 + ((7 - row) * 8)] is not None:
                return False
        return True

    def kingCaptured(self, color):
        king = None
        for piece in self.board:
            if isinstance(piece, King):
                if piece.color == color:
                    king = piece
        return True if king is None else False
