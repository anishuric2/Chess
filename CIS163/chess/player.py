from enum import Enum

class Player(Enum):
    """
    Represents the players in a chess game, offering an enumeration of the two possible players: BLACK and WHITE.

    Attributes:
        BLACK (int): Enum member representing the black player.
        WHITE (int): Enum member representing the white player.
    """
    BLACK = 0
    WHITE = 1

    def next(self):
        """
        Determines the next player, allowing for a switch between players in a cyclic manner.

        Returns:
            Player: The next player in sequence. If the current player is BLACK, returns WHITE, and vice versa.
        """
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]

