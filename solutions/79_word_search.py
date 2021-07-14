class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if self._dfs(board, word, 1, i, j, visited):
                        return True
                    visited.discard((i, j))
        return False
                
    def _dfs(self, board, word, idx, i, j, visited):
        if idx == len(word):
            return True
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and word[idx] == board[ni][nj] and (ni, nj) not in visited:
                visited.add((ni, nj))
                if self._dfs(board, word, idx+1, ni, nj, visited):
                    return True
                visited.discard((ni, nj))
        return False
