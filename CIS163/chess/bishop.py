from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Bishop(ChessPiece):
    """Represents a bishop chess piece.

    Inherits from ChessPiece and implements specific move validation logic for a bishop.
    """
    def __str__(self) -> str:
        """Returns a string representation of the bishop.

        Returns:
            str: A single character 'B' representing a bishop.
        """
        return "B"
    
    def type(self) -> str:
        """Returns the type of the chess piece.

        Returns:
            str: The word 'Bishop' indicating this is a bishop piece.
        """
        return "Bishop"
    
    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        """Checks if a move for the bishop is valid according to chess rules.

        The bishop moves diagonally any number of squares. It cannot jump over other pieces.

        Args:
            move (Move): The move to validate.
            board (List[List["ChessPiece"]]): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """

        if not super().is_valid_move(move, board):
            return False
        
        # If the bishop is moving diagonally
        if abs(move.from_row - move.to_row) == abs(move.from_col - move.to_col):
            # If the bishop is moving to the upper right
            if move.from_row > move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
                    return True
            # If the bishop is moving to the upper left
            if move.from_row > move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
                    return True
            # If the bishop is moving to the lower right
            if move.from_row < move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col + i] is not None:
                            return False
                    return True
            # If the bishop is moving to the lower left
            if move.from_row < move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
                    return True
        return False