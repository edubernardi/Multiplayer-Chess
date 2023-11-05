class Piece():
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column


class Pawn(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)
        self.firstMove = True

    def toString(self):
        return '♟' if self.color == 'black' else '♙'

    def validate(self, destination, row, column, board):
        direction = - 1 if self.color == 'black' else 1

        if destination is None:
            if (row == self.row + direction or ((row == self.row + (direction * 2)) and self.firstMove)) \
                    and self.column == column:
                self.firstMove = False
                return True
        else:
            if destination.color == self.color:
                return False
            if row == self.row + direction and column == self.column + 1:
                self.firstMove = False
                return True
            if row == self.row + direction and column == self.column - 1:
                self.firstMove = False
                return True
        return False


class Rook(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♜' if self.color == 'black' else '♖'

    def validate(self, destination, row, column, board):
        if destination is not None:
            if self.color == destination.color:
                return False
        if self.column == column or self.row == row:
            return board.clearPathLine(self.column, column, self.row, row)
        return False


class Bishop(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♝' if self.color == 'black' else '♗'

    def validate(self, destination, row, column, board):
        if destination is not None:
            if self.color == destination.color:
                return False
        if abs(column - self.column) == abs(row - self.row):
            return board.clearPathDiagonal(self.column, column, self.row, row)
        return False


class Knight(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♞' if self.color == 'black' else '♘'

    def validate(self, destination, row, column, board):
        if destination is not None:
            if self.color == destination.color:
                return False
        return abs(self.row - row) == 1 and abs(self.column - column) == 2 or\
               abs(self.row - row) == 2 and abs(self.column - column) == 1


class Queen(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♛' if self.color == 'black' else '♕'

    def validate(self, destination, row, column, board):
        if destination is not None:
            if self.color == destination.color:
                return False
        if abs(column - self.column) == abs(row - self.row):
            return board.clearPathDiagonal(self.column, column, self.row, row)
        if self.column == column or self.row == row:
            return board.clearPathLine(self.column, column, self.row, row)
        return False



class King(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♚' if self.color == 'black' else '***REMOVED***'

    def validate(self, destination, row, column, board):
        if destination is not None:
            if self.color == destination.color:
                return False
        return abs(self.row - row) == 1 and abs(self.column - column) == 0 or\
               abs(self.row - row) == 0 and abs(self.column - column) == 1 or\
               abs(self.row - row) == 1 and abs(self.column - column) == 1

