class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """DFS.
        """
        v = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    v.add((i, j))
                    if self.dfs(board, i, j, word[1:], v):
                        return True
                    v.remove((i, j))
        return False

    def dfs(self, board, i, j, word, v):
        if not word:
            return True
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == word[0] and (ni, nj) not in v:
                v.add((ni, nj))
                if self.dfs(board, ni, nj, word[1:], v):
                    return True
                v.remove((ni, nj))
        return False