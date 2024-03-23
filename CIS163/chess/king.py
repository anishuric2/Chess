from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class King(ChessPiece):
    """Represents a King chess piece."""

    def __str__(self) -> str:
        """Return a string representation of the King."""
        return "K"

    def type(self) -> str:
        """Return the type of the chess piece."""
        return "King"

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]) -> bool:
        """Check if the move is valid for the King.

        Args:
            move (Move): The move to be checked.
            board (List[List[ChessPiece]]): The current state of the chess board.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not super().is_valid_move(move, board):
            return False

        # If the king is moving one space in any direction
        if (
                abs(move.from_row - move.to_row) <= 1
                and abs(move.from_col - move.to_col) <= 1
        ):
            # If the destination is empty or occupied by the other player
            if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
            ):
                return True

        return False