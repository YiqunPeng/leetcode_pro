class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """Math.

        Running time: O(k) where k is the area of the board.
        """
        def count(i, j, m, n):
            s = 0
            for i in range(max(0, r-1), min(r+2, len(board))):
                for j in range(max(0, c-1), min(c+2, len(board[0]))):
                    if i == r and c == j:
                        continue
                    if abs(board[i][j]) == 1:
                        s += 1
            return s 
            
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                c = count(i, j, m, n)
                if board[i][j] == 1:
                    if c < 2 or c > 3:
                        board[i][j] = -1
                else:
                    if c == 3:
                        board[i][j] = 2
              
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
                