class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [[0] * n for i in range(2)]
        self.cols = [[0] * n for i in range(2)]
        self.d = [0, 0]
        self.subd = [0, 0]
        self.n = n
        self.winner = 0

        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.

        Running time: O(n).
        """
        if not self.winner:
            p = player - 1
            
            self.rows[p][row] += 1
            self.cols[p][col] += 1
            if row == col:
                self.d[p] += 1
            if row + col + 1 == self.n:
                self.subd[p] += 1 
                
            if self.n in [self.rows[p][row], self.cols[p][col], self.d[p], self.subd[p]]:
                self.winner = player
        
        return self.winner
