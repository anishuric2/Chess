from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Knight(ChessPiece):
    """Represents a knight chess piece, inheriting from ChessPiece."""
    def __str__(self) -> str:
        """String representation of the knight piece.

        Returns:
            str: A single character 'N' representing a knight.
        """
        return "N"
    
    def type(self) -> str:
        """Gets the type of the chess piece.

        Returns:
            str: The word 'Knight', indicating this is a knight piece.
        """
        return "Knight"
    
    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        """Validates a knight's move according to chess rules.

        Knights move in an L shape: two squares in one direction and then one square to the side,
        Knights can jump over other pieces.

        Args:
            move (Move): The move to validate.
            board (List[List["ChessPiece"]]): The chess board's current state.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not super().is_valid_move(move, board):
            return False
        
        # If the knight is moving in an L shape
        if (
            abs(move.from_row - move.to_row) == 2
            and abs(move.from_col - move.to_col) == 1
        ) or (
            abs(move.from_row - move.to_row) == 1
            and abs(move.from_col - move.to_col) == 2
        ):
            # If knight's destination is empty or occupied by the other player
            if (
                board[move.to_row][move.to_col] is None
                or board[move.to_row][move.to_col].player != self.player
            ):
                return True
        
        return False