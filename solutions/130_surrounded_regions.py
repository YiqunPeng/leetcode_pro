class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        borders = deque()
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'Y'
                borders.append((i, 0))
            if board[i][n-1] == 'O':
                board[i][n-1] = 'Y'
                borders.append((i, n-1))
        for j in range(1, n - 1):
            if board[0][j] == 'O':
                board[0][j] = 'Y'
                borders.append((0, j))
            if board[m-1][j] == 'O':
                board[m-1][j] = 'Y'
                borders.append((m-1, j))
        while borders:
            i, j = borders.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    board[ni][nj] = 'Y'
                    borders.append((ni, nj))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
