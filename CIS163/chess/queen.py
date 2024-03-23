from chess_piece import ChessPiece
from move import Move
from typing import List
from player import Player


class Queen(ChessPiece):
    """Represents a queen chess piece, capable of moving any number of squares along a row, column, or diagonal."""

    def __str__(self) -> str:
        """Provides a string representation of the queen piece.

        Returns:
            A single character 'Q' representing a queen.
        """
        return "Q"
    
    def type(self) -> str:
        """Gets the type of the chess piece.

        Returns:
            The word 'Queen', indicating this is a queen piece.
        """
        return "Queen"
    
    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]) -> bool:
        """Validates a queen's move according to chess rules.

        The queen can move any number of squares along a row, column, or diagonal,
        but cannot jump over other pieces. This method checks for the validity of the move based
        on these constraints.

        Args:
            move (Move): The move to validate.
            board (List[List[ChessPiece]]): The chess board's current state.

        Returns:
            bool: True if the move is valid according to queen's movement rules, False otherwise.
        """
        if not super().is_valid_move(move, board):
            return False
        
        # If the queen is moving horizontally
        if move.from_row == move.to_row:
            # If the queen is moving to the right
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
            # If the queen is moving to the left
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
        
        # If the queen is moving vertically
        elif move.from_col == move.to_col:
            # If the queen is moving upwards
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
            # If the queen is moving downwards
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
                
        # If the queen is moving diagonally
        if abs(move.from_row - move.to_row) == abs(move.from_col - move.to_col):
            # If the queen is moving to the upper right
            if move.from_row > move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
                    return True
            # If the queen is moving to the upper left
            if move.from_row > move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
                    return True
            # If the queen is moving to the lower right
            if move.from_row < move.to_row and move.from_col < move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col + i] is not None:
                            return False
                    return True
            # If the queen is moving to the lower left
            if move.from_row < move.to_row and move.from_col > move.to_col:
                # If the path is clear and the destination is empty or occupied by the other player
                if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player != self.player:
                    for i in range(1, abs(move.from_row - move.to_row)):
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
                    return True
        return False