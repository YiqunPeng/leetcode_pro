class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """Array.
        """
        stable = False
        while not stable:
            board, stable = self._crush(board)
            if not stable:
                board = self._drop(board)
        return board
    
    def _crush(self, board):
        """Running time: O(k) where k is the number of items in board.
        """
        m, n = len(board), len(board[0])
        crush = set()
        stable = True
        for i in range(m):
            for j in range(1, n - 1):
                if board[i][j] == 0:
                    continue
                if board[i][j-1] == board[i][j] == board[i][j+1]:
                    crush |= set([(i, j-1), (i, j), (i, j+1)])
        for j in range(n):
            for i in range(m - 2, 0, -1):
                if board[i][j] == 0:
                    break
                if board[i-1][j] == board[i][j] == board[i+1][j]:
                    crush |= set([(i-1, j), (i, j), (i+1, j)])
        if crush:
            stable = False
            for i, j in crush:
                board[i][j] = 0
        return board, stable
    
    def _drop(self, board):
        """Running time: O(k) where k is the number of items in board.
        """
        m, n = len(board), len(board[0])
        for j in range(n):
            c, p = m - 1, m - 1
            while p >= 0:
                if board[p][j] == 0:
                    p -= 1
                else:
                    board[c][j] = board[p][j]
                    p -= 1
                    c -= 1
            while c >= 0:
                board[c][j] = 0
                c -= 1
        return board
