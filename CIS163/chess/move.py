class Move:
    def __init__(self, from_row, from_col, to_row, to_col):
        """
        Represents a move in a game of chess, detailing the start and end positions.

        Attributes:
            from_row (int): The starting row of the move.
            from_col (int): The starting column of the move.
            to_row (int): The destination row of the move.
            to_col (int): The destination column of the move.
        """
        self.from_row = from_row
        self.from_col = from_col
        self.to_row = to_row
        self.to_col = to_col

    def __str__(self):
        """
        Initializes a new instance of the Move class with specified start and end positions.

        Args:
            from_row (int): The starting row of the move.
            from_col (int): The starting column of the move.
            to_row (int): The destination row of the move.
            to_col (int): The destination column of the move.
        """
        output = f'Move [from_row={self.from_row}, from_col={self.from_col}'
        output += f', to_row={self.to_row}, to_col={self.to_col}]'
        return output
