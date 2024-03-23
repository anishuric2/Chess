
from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Rook(ChessPiece):
    """Represents a rook chess piece, inheriting from ChessPiece."""
    def __str__(self) -> str:
        """String representation of the rook piece.

        Returns:
            str: A single character 'R' representing a rook.
        """
        return "R"

    def type(self) -> str:
        """Gets the type of the chess piece.

        Returns:
            str: The word 'Rook', indicating this is a rook piece.
        """
        return "Rook"

    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        """Validates a rook's move according to chess rules.

        Rooks move any number of squares along a row or column, but cannot jump over other pieces.

        Args:
            move (Move): The move to validate.
            board (List[List["ChessPiece"]]): The chess board's current state.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not super().is_valid_move(move, board):
            return False

        # If the rook is moving horizontally
        if move.from_row == move.to_row:
            # If the rook is moving to the right
            if move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                for col in range(move.from_col + 1, move.to_col):
                    if board[move.from_row][col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True
            # If the rook is moving to the left
            elif move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                for col in range(move.to_col + 1, move.from_col):
                    if board[move.from_row][col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True

        # If the rook is moving vertically
        elif move.from_col == move.to_col:
            # If the rook is moving upwards
            if move.from_row > move.to_row:
                # If the path is clear and the destination is empty or occupied by the other player
                for row in range(move.to_row + 1, move.from_row):
                    if board[row][move.from_col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True
            # If the rook is moving downwards
            elif move.from_row < move.to_row:
                # If the path is clear and the destination is empty or occupied by the other player
                for row in range(move.from_row + 1, move.to_row):
                    if board[row][move.from_col] is not None:
                        return False
                if (
                    board[move.to_row][move.to_col] is None
                    or board[move.to_row][move.to_col].player != self.player
                ):
                    return True

        return False
