class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        boader = []
        self._mark_island(A, boader)
        return self._bfs(A, boader)
    
    def _mark_island(self, A, boader):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A[i][j] = -1
                    return self._dfs(A, i, j, boader)
    
    def _dfs(self, A, i, j, boader):
        if self._on_border(A, i, j):
            boader.append((i, j))
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < len(A) and 0 <= nj < len(A[0]) and A[ni][nj] == 1:
                A[ni][nj] = -1
                self._dfs(A, ni, nj, boader)
    
    def _bfs(self, A, boader):
        q = deque(boader)
        seen = set()
        res = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                if A[i][j] == 1:
                    return res - 1
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= ni < len(A) and 0 <= nj < len(A[0]) and A[ni][nj] != -1 and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        q.append((ni, nj))
            res += 1
    
    def _on_border(self, A, i, j):
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < len(A) and 0 <= nj < len(A[0]) and A[ni][nj] == 0:
                return True
        return False
