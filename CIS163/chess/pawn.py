from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Pawn(ChessPiece):
    """Represents a pawn chess piece, inheriting from ChessPiece."""
    def __str__(self) -> str:
        """String representation of the pawn piece.

        Returns:
            str: A single character 'P' representing a pawn.
        """
        return "P"

    def type(self) -> str:
        """Gets the type of the chess piece.

        Returns:
            str: The word 'Pawn', indicating this is a pawn piece.
        """
        return "Pawn"

    def is_valid_move(self, move: Move, board: List[List["ChessPiece"]]) -> bool:
        """Validates a pawn's move according to chess rules.

        Pawns move forward one square, with the option to move two squares from their initial position.
        They capture one square diagonally. Special rules apply for capturing en passant (not implemented here).

        Args:
            move (Move): The move to validate.
            board (List[List["ChessPiece"]]): The chess board's current state.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not super().is_valid_move(move, board):
            return False

        # If the pawn is white
        if self.player == Player.WHITE:
            # if pawn is moving forward and not taking
            if move.from_col == move.to_col:
                # if pawn is moving forward 1 space
                if move.from_row - move.to_row == 1:
                    # if the space is empty
                    if board[move.to_row][move.to_col] is None:
                        return True
                # if pawn is moving forward 2 spaces
                elif move.from_row == 6 and move.to_row == 4:
                    # if the space is empty
                    if (
                        board[move.to_row][move.to_col] is None
                        and board[move.to_row + 1][move.to_col] is None
                    ):
                        return True

            # if pawn is taking
            elif (
                abs(move.from_col - move.to_col) == 1
                and move.from_row - move.to_row == 1
            ):
                # if the piece belongs to the other player
                if (
                    board[move.to_row][move.to_col] is not None
                    and board[move.to_row][move.to_col].player == Player.BLACK
                ):
                    return True

        # If the pawn is black
        elif self.player == Player.BLACK:
            # if pawn is moving forward and not taking
            if move.from_col == move.to_col:
                # if pawn is moving forward 1 space
                if move.to_row - move.from_row == 1:
                    # if the space is empty
                    if board[move.to_row][move.to_col] is None:
                        return True
                # if pawn is moving forward 2 spaces
                elif move.from_row == 1 and move.to_row == 3:
                    # if the space is empty
                    if (
                        board[move.to_row][move.to_col] is None
                        and board[move.to_row - 1][move.to_col] is None
                    ):
                        return True
            # if pawn is taking
            elif (
                abs(move.from_col - move.to_col) == 1
                and move.to_row - move.from_row == 1
            ):
                # if the piece belongs to the other player
                if (
                    board[move.to_row][move.to_col] is not None
                    and board[move.to_row][move.to_col].player == Player.WHITE
                ):
                    return True

        return False
