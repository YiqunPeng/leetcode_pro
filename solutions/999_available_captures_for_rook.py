class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        """Array.

        Running time: O(n^2) where n is the size of board.
        """
        ri, rj = self._find_rook(board)
        res = 0
        l = rj - 1
        while l >= 0:
            if board[ri][l] == 'B':
                break
            if board[ri][l] == 'p':
                res += 1
                break
            l -= 1
        r = rj + 1
        while r < 8:
            if board[ri][r] == 'B':
                break
            if board[ri][r] == 'p':
                res += 1
                break
            r += 1
        u = ri - 1
        while u >= 0:
            if board[u][rj] == 'B':
                break
            if board[u][rj] == 'p':
                res += 1
                break
            u -= 1
        d = ri + 1
        while d < 8:
            if board[d][rj] == 'B':
                break
            if board[d][rj] == 'p':
                res += 1
                break
            d += 1
        return res
            
    def _find_rook(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return i, j
