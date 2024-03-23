import unittest


from chess_model import ChessModel
from pawn import Pawn
from player import Player
from move import Move
from king import King
from queen import Queen
from rook import Rook
from bishop import Bishop
from knight import Knight

if __name__ == "__main__":
    unittest.main()

# These test should return True
class TestInCheck(unittest.TestCase):
    def setUp(self):
        # Initialize a chess model
        self.chess_game = ChessModel()

    def clear_board(self):
        # Clear the board
        for row in range(self.chess_game.nrows):
            for col in range(self.chess_game.ncols):
                self.chess_game.board[row][col] = None

    def test_IncheckRook(self):
        self.clear_board()
        # Set current player to Black
        self.chess_game.current_player = Player.BLACK

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(0, 6, Rook(Player.WHITE))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.BLACK))

    def test_InCheckPawn(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 1, King(Player.BLACK))
        self.chess_game.set_piece(1, 2, Pawn(Player.WHITE))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.BLACK))

    def test_InCheckBishop(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(7, 7, Bishop(Player.WHITE))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.BLACK))

    def test_InCheckQueen(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(7, 7, Queen(Player.WHITE))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.BLACK))

    def test_InCheckKnight(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(1, 2, Knight(Player.WHITE))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.BLACK))

# checks the same test but different color
    def test_InCheckKnightColor(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.WHITE))
        self.chess_game.set_piece(1, 2, Knight(Player.BLACK))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.WHITE))


    # incheck with 1 pieces
    def test_InCheck1(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(1, 1, Pawn(Player.BLACK))
        self.chess_game.set_piece(1, 0, Pawn(Player.BLACK))
        self.chess_game.set_piece(1, 2, Pawn(Player.BLACK))
        self.chess_game.set_piece(0, 6, Rook(Player.WHITE))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.BLACK))


    # incheck with 3 pieces
    def test_InCheck3(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 1, King(Player.BLACK))
        self.chess_game.set_piece(1, 1, Queen(Player.WHITE))
        self.chess_game.set_piece(1, 0, Queen(Player.WHITE))
        self.chess_game.set_piece(1, 2, Queen(Player.BLACK))
        self.chess_game.set_piece(0, 6, Rook(Player.WHITE))

        # Check if the game is complete
        self.assertTrue(self.chess_game.in_check(Player.BLACK))

    # Checkmate

    def test_InCheckmate1(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(1, 1, Pawn(Player.BLACK))
        self.chess_game.set_piece(1, 0, Pawn(Player.BLACK))
        self.chess_game.set_piece(1, 2, Pawn(Player.BLACK))
        self.chess_game.set_piece(0, 6, Rook(Player.WHITE))
        self.chess_game.move(Move(0,6, 0,5))
        # Check if the game is complete
        self.assertTrue(self.chess_game.is_complete())

    # Threatened immediate check with 2 pieces
    # Pawn and knight are check if king moves
    def test_InCheckmateBy2(self):
        self.clear_board()

        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(1, 0, Pawn(Player.BLACK))
        self.chess_game.set_piece(2, 0, Pawn(Player.WHITE))
        self.chess_game.set_piece(0, 7, Rook(Player.WHITE))
        self.chess_game.set_piece(1, 1, Queen(Player.WHITE))
        self.chess_game.set_piece(2, 2, Knight(Player.WHITE))
        self.chess_game.move(Move(0, 7, 0,6))

        self.assertTrue(self.chess_game.is_complete())

    # Threatened immediate check with 3 pieces
    # Rook immediate checks if it moves
    def test_InCheckmateBy3(self):
        self.clear_board()

        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(3, 0, Rook(Player.WHITE))
        self.chess_game.set_piece(1, 1, Pawn(Player.WHITE))
        self.chess_game.set_piece(0, 2, Queen(Player.WHITE))
        self.chess_game.set_piece(1, 2, Rook(Player.WHITE))
        self.chess_game.set_piece(2, 1, Knight(Player.WHITE))

        self.chess_game.move(Move(0, 2, 0,4))

        self.assertTrue(self.chess_game.is_complete())


    # Threatened immediate check with 3 pieces
    # Rook immediate checks if it moves
    def test_InCheckmateBy4(self):
        self.clear_board()

        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(3, 0, Rook(Player.WHITE))
        self.chess_game.set_piece(1, 1, Pawn(Player.WHITE))
        self.chess_game.set_piece(0, 2, Queen(Player.WHITE))
        self.chess_game.set_piece(1, 1, Bishop(Player.WHITE))
        self.chess_game.set_piece(2, 1, Knight(Player.WHITE))

        self.chess_game.move(Move(0, 3, 0,4))

        self.assertTrue(self.chess_game.is_complete())

    # checkmate with 4 pieces
    def test_InCheckMate5(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 1, King(Player.BLACK))
        self.chess_game.set_piece(1, 1, Queen(Player.WHITE))
        self.chess_game.set_piece(1, 0, Queen(Player.WHITE))
        self.chess_game.set_piece(1, 2, Queen(Player.WHITE))
        self.chess_game.set_piece(0, 6, Rook(Player.WHITE))
        self.chess_game.move(Move(0, 6, 0, 5))

        # Check if the game is complete
        self.assertTrue(self.chess_game.is_complete())


# in check Block
    def test_InCheckPawn_blocked(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 1, King(Player.BLACK))
        self.chess_game.set_piece(1, 2, Pawn(Player.WHITE))
        # Add a piece blocking the pawn's attack
        self.chess_game.set_piece(2, 3, Pawn(Player.WHITE))

        self.chess_game.move(Move(2, 3, 0, 1))

        # Check if the game is complete
        self.assertFalse(self.chess_game.in_check(Player.BLACK))

    def test_InCheckBishop_blocked(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(7, 7, Bishop(Player.WHITE))
        # Add a piece blocking the bishop's attack
        self.chess_game.set_piece(5, 5, Pawn(Player.BLACK))

        # Check if the game is complete
        self.assertFalse(self.chess_game.in_check(Player.BLACK))

    def test_InCheckQueen_blocked(self):
        self.clear_board()

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(7, 7, Queen(Player.WHITE))
        # Add a piece blocking the queen's attack
        self.chess_game.set_piece(4, 4, Pawn(Player.BLACK))

        # Check if the game is complete
        self.assertFalse(self.chess_game.in_check(Player.BLACK))

    def test_checkmateRook_blocked(self):
        self.clear_board()
        # Set current player to Black
        self.chess_game.current_player = Player.BLACK

        # Set Pieces
        self.chess_game.set_piece(0, 0, King(Player.BLACK))
        self.chess_game.set_piece(0, 6, Rook(Player.WHITE))
        # Add a piece blocking the rook's attack
        self.chess_game.set_piece(0, 5, Pawn(Player.BLACK))

        # Check if the game is complete
        self.assertFalse(self.chess_game.in_check(Player.BLACK))

# This test simulates an entire game. White Wins in checkmate
    def test_simulateGame1(self):
        # black pawn
        self.chess_game.move(Move(6,4,4,4))
        # black pawn
        self.chess_game.move(Move(1,4,3,4))
        # White queen
        self.chess_game.move(Move(7,3,3,7))
        #black pawn
        self.chess_game.move(Move(1,1,2,1))
        #White bishop
        self.chess_game.move(Move(7,5,4,2))
        # black pawn
        self.chess_game.move(Move(1, 0, 2, 0))
        # White queen
        self.chess_game.move(Move(3,7,1,5))

        # Check if the game is complete
        self.assertTrue(self.chess_game.is_complete())

    # White loses
    def test_simulateGame2(self):
        # White pawn
        self.chess_game.move(Move(6,5,5,5))
        # black pawn
        self.chess_game.move(Move(1,4,3,4))
        # White pawn
        self.chess_game.move(Move(6,6,4,6))
        # Black Queen
        self.chess_game.move(Move(0,3,4,7))

        # Check if the game is complete
        self.assertTrue(self.chess_game.is_complete())


    # Checks the pawn promotion
    def test_PawnPromotion(self):
        self.clear_board()

        self.chess_game.set_piece(1, 0, Pawn(Player.WHITE))
        # Move the pawn into row 0
        self.chess_game.move(Move(1, 0, 0, 0))

        promoted_piece = self.chess_game.piece_at(0, 0)
        self.assertIsInstance(promoted_piece, Queen)
        self.assertEqual(promoted_piece.player, Player.WHITE)


    # Test invalid moves

    def test_move_out_of_bounds(self):
        """Test moving a piece out of the chess board's boundaries."""
        self.chess_game.set_piece(0, 0, Rook(Player.WHITE))
        invalid_move = Move(0, 0, -1, -1)  # Attempt to move rook out of bounds
        self.assertFalse(self.chess_game.is_valid_move(invalid_move))

    def test_move_to_occupied_spot_same_color(self):
        """Test moving a piece to a spot already occupied by a piece of the same color."""
        self.chess_game.set_piece(0, 0, Rook(Player.WHITE))
        self.chess_game.set_piece(0, 1, Pawn(Player.WHITE))  # Adjacent spot occupied by same color
        invalid_move = Move(0, 0, 0, 1)  # Attempt to move rook to occupied spot
        self.assertFalse(self.chess_game.is_valid_move(invalid_move))

    def test_pawn_invalid_capture_move(self):
        """Test pawn attempting to capture forward instead of diagonally."""
        self.chess_game.set_piece(1, 0, Pawn(Player.WHITE))
        self.chess_game.set_piece(2, 0, Pawn(Player.BLACK))  # Enemy pawn directly ahead
        invalid_move = Move(1, 0, 2, 0)  # Pawn attempts to capture forward
        self.assertFalse(self.chess_game.is_valid_move(invalid_move))

    def test_knight_invalid_move_pattern(self):
        """Test knight attempting to move in a pattern that's not L-shaped."""
        self.chess_game.set_piece(0, 1, Knight(Player.WHITE))
        invalid_move = Move(0, 1, 2, 1)  # Attempt to move knight in a straight line
        self.assertFalse(self.chess_game.is_valid_move(invalid_move))

    def test_bishop_invalid_move_pattern(self):
        """Test bishop attempting to move horizontally instead of diagonally."""
        self.chess_game.set_piece(0, 2, Bishop(Player.WHITE))
        invalid_move = Move(0, 2, 0, 4)  # Attempt to move bishop horizontally
        self.assertFalse(self.chess_game.is_valid_move(invalid_move))

    def test_queen_invalid_move_pattern(self):
        """Test queen attempting to move in a pattern not allowed (like a knight)."""
        self.chess_game.set_piece(0, 3, Queen(Player.WHITE))
        invalid_move = Move(0, 3, 2, 2)  # Attempt to move queen like a knight
        self.assertFalse(self.chess_game.is_valid_move(invalid_move))

    def test_king_invalid_move_pattern(self):
        """Test king attempting to move more than one square away."""
        self.chess_game.set_piece(0, 4, King(Player.WHITE))
        invalid_move = Move(0, 4, 2, 4)  # Attempt to move king two squares forward
        self.assertFalse(self.chess_game.is_valid_move(invalid_move))
