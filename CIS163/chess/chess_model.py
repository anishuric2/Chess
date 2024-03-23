from enum import Enum
import random
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King



class MoveValidity(Enum):
    Valid = 1
    Invalid = 2
    MovingIntoCheck = 3
    StayingInCheck = 4

    def __str__(self):
        if self.value == 1:
            return "Valid move."
        elif self.value == 2:
            return "Invalid move."
        elif self.value == 3:
            return "Invalid -- cannot move into check."
        elif self.value == 4:
            return "Invalid -- must move out of check."
        else:
            return "Unknown move validity."


class ChessModel:

    """Represents the model of a chess game, managing the game state, player turns, and move validation.

    Attributes:
        __nrows (int): Number of rows on the chess board.
        __ncols (int): Number of columns on the chess board.
        __player (Player): The current player (either Player.WHITE or Player.BLACK).
        __message_code (MoveValidity): The validity status of the last move attempted.
        board (list): A 2D list representing the chess board with pieces.
        move_history (list): A list storing the history of moves made during the game.
    """

    def __init__(self):

        """Initializes a new chess game with a standard board setup."""

        self.__nrows = 8
        self.__ncols = 8
        self.__player = Player.WHITE
        self.__message_code = MoveValidity.Valid
        self.board = [[None] * self.__ncols for _ in range(self.__nrows)]
        self.setup_standard_board()
        self.move_history = []
        self.temp_board = None

    def setup_standard_board(self):
        """Sets up the chess board with pieces in their standard starting positions."""

        # Set up pawns
        for col in range(self.ncols):
            self.set_piece(1, col, Pawn(Player.BLACK))
            self.set_piece(self.nrows - 2, col, Pawn(Player.WHITE))

        #Set up other pieces
        self.set_piece(0, 0, Rook(Player.BLACK))
        self.set_piece(0, 1, Knight(Player.BLACK))
        self.set_piece(0, 2, Bishop(Player.BLACK))
        self.set_piece(0, 3, Queen(Player.BLACK))
        self.set_piece(0, 4, King(Player.BLACK))
        self.set_piece(0, 5, Bishop(Player.BLACK))
        self.set_piece(0, 6, Knight(Player.BLACK))
        self.set_piece(0, 7, Rook(Player.BLACK))
        self.set_piece(7, 0, Rook(Player.WHITE))
        self.set_piece(7, 1, Knight(Player.WHITE))
        self.set_piece(7, 2, Bishop(Player.WHITE))
        self.set_piece(7, 3, Queen(Player.WHITE))
        self.set_piece(7, 4, King(Player.WHITE))
        self.set_piece(7, 5, Bishop(Player.WHITE))
        self.set_piece(7, 6, Knight(Player.WHITE))
        self.set_piece(7, 7, Rook(Player.WHITE))






    @property
    def nrows(self) -> int:
        """int: The number of rows on the chess board."""
        return self.__nrows

    @property
    def ncols(self) -> int:
        """int: The number of columns on the chess board."""
        return self.__ncols

    @property
    def current_player(self) -> Player:
        """Player: The player currently taking their turn."""
        return self.__player

    @property
    def messageCode(self) -> MoveValidity:
        """MoveValidity: The validity status of the last move attempted."""
        return self.__message_code

    @nrows.setter
    def nrows(self, value: int):
        self.__nrows = value

    @ncols.setter
    def ncols(self, value: int):
        self.__ncols = value

    @current_player.setter
    def current_player(self, value: Player):
        self.__player = value

    @messageCode.setter
    def messageCode(self, value: MoveValidity):
        self.__message_code = value

    def is_valid_move(self, move: Move) -> bool:

        """Checks if a given move is valid.

        Validates the move based on the current board state, ensuring it does not result in the player
        moving into check.

        Args:
            move (Move): The move to validate.

        Returns:
            bool: True if the move is valid, False otherwise.
        """

        # Get the piece at the source location of the move
        piece = self.board[move.from_row][move.from_col]

        # Check if there is a piece at the source location,
        # if it's not the current player's piece, or if it's not a valid ChessPiece
        if piece is None or not isinstance(piece, ChessPiece) or piece.player != self.__player:
            # Set message code to indicate an invalid move
            self.__message_code = MoveValidity.Invalid
            return False

        # Check if the piece allows this move
        if not piece.is_valid_move(move, self.board):
            # Set message code to indicate an invalid move
            self.__message_code = MoveValidity.Invalid
            return False

        # Simulate the move to check for moving into check
        simulated_board = []
        for row in self.board:
            simulated_row = []
            for item in row:
                simulated_row.append(item)
            simulated_board.append(simulated_row)

        # Make the move on the simulated board
        simulated_board[move.to_row][move.to_col] = piece
        simulated_board[move.from_row][move.from_col] = None

        # Check if the move puts the player's own king in check
        if self.in_check(self.__player, simulated_board):
            # Set message code to indicate moving into check
            self.__message_code = MoveValidity.MovingIntoCheck
            return False

        # Set message code to indicate a valid move
        self.__message_code = MoveValidity.Valid
        return True

    def is_complete(self) -> bool:

        """Determines if the game is complete, either by checkmate or stalemate.

        Iterates over all pieces for the current player to check if any valid moves are available.
        If no valid moves are available and the player is in check, it's checkmate. If no moves are
        available but the player is not in check, it's stalemate.

        Returns:
            bool: True if the game is complete, False otherwise.
        """

        # Iterate over each cell on the board
        for row in range(self.__nrows):
            for col in range(self.__ncols):
                # Get the piece at the current cell
                piece = self.board[row][col]

                # Check if there's a piece at the cell, and it belongs to the current player
                if piece and piece.player == self.__player:
                    # Iterate over all possible destination cells
                    for to_row in range(self.__nrows):
                        for to_col in range(self.__ncols):
                            # Create a move from the current cell to the destination cell
                            move = Move(row, col, to_row, to_col)

                            # Check if the move is valid
                            if self.is_valid_move(move):
                                # If there's at least one valid move for the current player, the game is not complete
                                return False
        # If no valid move is found for the current player, check if the player is in check
        if self.in_check(self.__player):
            return True
        else:
            return False

    def move(self, move: Move):
        """Executes a chess move on the board, including pawn promotion and turn switching.

        Args:
            move (Move): The move to be executed.

        Note:
            - If the game is already in a checkmate or stalemate state (`is_complete` returns True),
              no action is taken.
            - The method also handles pawn promotion to a queen if a pawn reaches the opposite end of the board.
        """

        # Check if the game is already in checkmate
        if self.is_complete():
            return

        # Make a copy of the current board state
        current_state = []
        for row in self.board:
            current_state.append(row[:])

        # Make the move on the board
        self.board[move.to_row][move.to_col] = self.board[move.from_row][move.from_col]
        self.board[move.from_row][move.from_col] = None

        # Check for pawn promotion to Queen
        moved_piece = self.piece_at(move.to_row, move.to_col)
        if isinstance(moved_piece, Pawn):
            if moved_piece.player == Player.WHITE:
                if move.to_row == 0:
                    promoted_piece = Queen(moved_piece.player)
                    self.board[move.to_row][move.to_col] = promoted_piece
            elif moved_piece.player == Player.BLACK:
                if move.to_row == 7:
                    promoted_piece = Queen(moved_piece.player)
                    self.board[move.to_row][move.to_col] = promoted_piece

        # Set the next player
        self.set_next_player()

        # Save the move and the recorded board state to the move history
        self.move_history.append((current_state, move))

    def in_check(self, player: Player, board=None):
        """Determines if a player's king is in check.

        Args:
            player (Player): The player to check for being in check.
            board (list, optional): A specific board configuration to check. Defaults to the current board.

        Returns:
            bool: True if the player's king is in check, False otherwise.
        """

        # If no board is provided, use the current board
        if board is None:
            board = self.board

        # Initialize variables to store the king's position
        king_row, king_col = None, None

        # Find the position of the king of the specified player on the board
        for row in range(self.__nrows):
            for col in range(self.__ncols):
                piece = board[row][col]
                if isinstance(piece, King) and piece.player == player:
                    king_row, king_col = row, col
                    break
            if king_row is not None:
                break

        # If the king's position is not found, return False (not in check)
        if king_row is None or king_col is None:
            return False

        # Check if any opponent's piece can attack the king
        for row in range(self.__nrows):
            for col in range(self.__ncols):
                piece = board[row][col]
                # Check if there is a piece at the current position, and it belongs to the opponent
                if piece and piece.player != player:
                    # Create a move from the opponent's piece to the king's position
                    move = Move(row, col, king_row, king_col)
                    # Check if the move is valid for the opponent's piece, i.e., it can attack the king
                    if piece.is_valid_move(move, board):
                        return True

        # If no opponent's piece can attack the king, return False (not in check)
        return False


    # ChessPiece method -> returns the piece at the given row and col
    def piece_at(self, row: int, col: int) -> ChessPiece:
        """Retrieves the chess piece at a specified board location.

        Args:
            row (int): The row of the piece.
            col (int): The column of the piece.

        Raises:
            TypeError: If the object at the specified location is not a valid ChessPiece.

        Returns:
            ChessPiece: The chess piece at the specified location, or None if the location is empty.
        """

        # Return None if coordinates are out of bounds
        if not (0 <= row < self.nrows) or not (0 <= col < self.ncols):
            return None

        piece = self.board[row][col]

        if piece is None:
            return None

        if not isinstance(piece, ChessPiece):
            raise TypeError("Invalid piece found at the specified location.")
        return piece

    def set_next_player(self):
        """Switches the turn to the next player."""
        if self.current_player == Player.WHITE:
            self.__player = Player.BLACK
        else:
            self.__player = Player.WHITE

    # Check if row and col are in bounds, raise a  ValueError if not
    # make sure that a piece is a ChessPiece. if not, raise a TypeError

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        """Places a chess piece on the board at the specified location.

        Args:
            row (int): The row to place the piece in.
            col (int): The column to place the piece in.
            piece (ChessPiece): The piece to place on the board.

        Raises:
            ValueError: If the specified row or column is out of bounds.
            TypeError: If the specified piece is not an instance of ChessPiece.
        """

        if row < 0 or row >= self.__nrows or col < 0 or col >= self.__ncols:
            raise ValueError("Row and col are out of bounds.")

        if not (piece is None or isinstance(piece, ChessPiece)):
            raise TypeError("Piece is not a ChessPiece.")

        self.board[row][col] = piece

    def undo(self):
        """Reverts the last move made in the game.

        Raises:
            UndoException: If there are no moves to undo.
        """

        if not self.move_history:
            raise UndoException("No moves to undo")
        # Retrieve the last move and board state from the history
        last_state, last_move = self.move_history.pop()

        # Restore the previous board state using deep copy
        self.board = []
        for row in last_state:
            self.board.append(row[:])

        # Switch back to the player who made the undone move
        self.set_next_player()


class UndoException(Exception):
    """Exception raised when an attempt is made to undo a move, but no moves are available to undo."""

    def __init__(self, message="No moves left to undo"):
        """Initializes an UndoException with an optional message.

        Args:
            message (str, optional): A message describing the exception. Defaults to a standard message.
        """

        self.message = message
        super().__init__(self.message)


class ChessAi:
    def __init__(self, model: ChessModel):
        self.model = model

    def make_move(self):
        """Attempts to make a move for the AI player."""

        # Check if the game is complete
        if self.model.is_complete():
            return

        # Attempt to make a random move
        while True:
            # Generate random row and column values for the move
            from_row = random.randint(0, self.model.nrows - 1)
            from_col = random.randint(0, self.model.ncols - 1)
            to_row = random.randint(0, self.model.nrows - 1)
            to_col = random.randint(0, self.model.ncols - 1)

            # Create a move from the generated values
            move = Move(from_row, from_col, to_row, to_col)

            # Check if the move is valid
            if self.model.is_valid_move(move):
                # Make the move on the board
                self.model.move(move)
                break

        # Check if the game is complete after the move
        if self.model.is_complete():
            return