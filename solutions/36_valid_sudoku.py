class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [set() for i in range(n)]
        col = [set() for i in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j]:
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
        c = 0
        nsqrt = int(n ** 0.5)
        while c < n:
            s = set()
            for i in range(c // nsqrt * nsqrt, c // nsqrt * nsqrt + nsqrt):
                for j in range(c % nsqrt * nsqrt, c % nsqrt * nsqrt + nsqrt):
                    if board[i][j] != '.':
                        if board[i][j] in s:
                            return False
                        s.add(board[i][j])
            c += 1
        return True
