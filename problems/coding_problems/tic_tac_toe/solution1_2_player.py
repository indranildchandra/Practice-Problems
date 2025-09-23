# Question: For every move in a Tic-Tac-Toe game, evaluate and confirm if the game ended based on last move and if yes then which player won.

# Solution:
# Time per move: O(1)
# Space: O(N)

class TicTacToeTwoPlayer:
    def __init__(self, n: int = 3):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Make a move for player (1 or 2) at (row, col).
        Returns:
            0 if no winner yet,
            player id (1 or 2) if that player wins with this move.
        """
        val = 1 if player == 1 else -1

        self.rows[row] += val
        self.cols[col] += val
        if row == col:
            self.diag += val
        if row + col == self.n - 1:
            self.anti_diag += val

        # Check any of four counters reached absolute n
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diag) == self.n or
            abs(self.anti_diag) == self.n):
            return player
        return 0

# Example
g = TicTacToeTwoPlayer(3)
print(g.move(0,0,1))  # 0
print(g.move(1,1,2))  # 0
print(g.move(0,1,1))  # 0
print(g.move(0,2,1))  # 1 -> player 1 wins
