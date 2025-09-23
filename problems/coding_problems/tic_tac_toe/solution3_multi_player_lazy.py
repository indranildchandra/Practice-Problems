# Question: For every move in a Tic-Tac-Toe game, evaluate and confirm if the game ended based on last move and if yes then which player won.

# Solution:
# Idea: only allocate counters for a player when they make a move; store counters in dictionaries (sparse)
# Time per move: O(1)
# Space: O(K) where K is number of distinct (player,row/col/diag) entries seen --> memory efficient when many players but sparse moves


class TicTacToeMultiLazy:
    def __init__(self, n: int = 3):
        self.n = n
        # per-player sparse counters: player -> {row_idx: count}
        self.rows = {}        # dict[player] -> dict(row -> count)
        self.cols = {}        # dict[player] -> dict(col -> count)
        self.diag = {}        # dict[player] -> count
        self.anti = {}        # dict[player] -> count

    def _ensure_player(self, player: int):
        if player not in self.rows:
            self.rows[player] = {}
            self.cols[player] = {}
            self.diag[player] = 0
            self.anti[player] = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Make a move for player (integer id) at (row, col).
        Returns: 0 if no winner, else player id.
        """
        self._ensure_player(player)

        # update row count
        rmap = self.rows[player]
        rmap[row] = rmap.get(row, 0) + 1

        # update col count
        cmap = self.cols[player]
        cmap[col] = cmap.get(col, 0) + 1

        # diag
        if row == col:
            self.diag[player] = self.diag.get(player, 0) + 1

        # anti-diag
        if row + col == self.n - 1:
            self.anti[player] = self.anti.get(player, 0) + 1

        # check win condition for this player only (O(1))
        if (rmap[row] == self.n or
            cmap[col] == self.n or
            self.diag.get(player, 0) == self.n or
            self.anti.get(player, 0) == self.n):
            return player
        return 0

# Example (3 players possible)
game = TicTacToeMultiLazy(3)
print(game.move(0,0,1))  # 0
print(game.move(1,1,2))  # 0
print(game.move(0,1,1))  # 0
print(game.move(0,2,1))  # 1 -> player 1 wins
