# Question: For every move in a Tic-Tac-Toe game, evaluate and confirm if the game ended based on last move and if yes then which player won.

# Solution:
# Time per move: O(1)
# Space: O(N)

from collections import defaultdict

class TicTacToeMulti:
    def __init__(self, n: int = 3, players: int = 2):
        self.n = n
        self.players = players

        # For each player, track rows, cols, diag, anti_diag counts
        self.rows = defaultdict(lambda: [0] * n)
        self.cols = defaultdict(lambda: [0] * n)
        self.diag = defaultdict(int)
        self.anti_diag = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player makes a move at (row, col).
        Return:
            0 if no one wins,
            player (id) if that player wins.
        """
        self.rows[player][row] += 1
        self.cols[player][col] += 1

        if row == col:
            self.diag[player] += 1
        if row + col == self.n - 1:
            self.anti_diag[player] += 1

        # Check win condition in O(1) for this player
        if (self.rows[player][row] == self.n or
            self.cols[player][col] == self.n or
            self.diag[player] == self.n or
            self.anti_diag[player] == self.n):
            return player

        return 0


# Example usage:
game = TicTacToeMulti(n=3, players=3)

print(game.move(0, 0, 1))  # -> 0
print(game.move(1, 1, 2))  # -> 0
print(game.move(0, 1, 1))  # -> 0
print(game.move(2, 2, 3))  # -> 0
print(game.move(0, 2, 1))  # -> 1 (Player 1 wins)
