class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """Math.

        Running time: O(k) where k is the area of the board.
        """
        def count(i, j, m, n):
            c = 0
            for ni, nj in [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1, j+1)]:
                if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                    c += 1
            return c    
            
        
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
                