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

    def validate(self, destination, row, column):
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

    def validate(self, destination):
        return


class Bishop(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♝' if self.color == 'black' else '♗'

    def validate(self, destination):
        return


class Knight(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♞' if self.color == 'black' else '♘'

    def validate(self, destination):
        return


class Queen(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♛' if self.color == 'black' else '♕'

    def validate(self, destination):
        return


class King(Piece):
    def __init__(self, color, row, column):
        Piece.__init__(self, color, row, column)

    def toString(self):
        return '♚' if self.color == 'black' else '***REMOVED***'

    def validate(self, destination):
        return
