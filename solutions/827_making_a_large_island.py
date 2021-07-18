class Solution:
    
    def __init__(self):
        self.islands = {0: 0}
        self.index = 2
        self.grid = None

    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.grid = grid
        m, n = len(self.grid), len(self.grid[0])
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 1:
                    area = self._dfs(i, j)
                    self.islands[self.index] = area
                    self.index += 1
        res = max(self.islands.values())
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 0:
                    idx = set([self.grid[ni][nj] for ni, nj in self._get_valid_next(i, j)])
                    res = max(res, sum(self.islands[a] for a in idx) + 1)
        return res
    
    def _dfs(self, i, j):
        self.grid[i][j] = self.index
        area = 1
        for ni, nj in self._get_valid_next(i, j):
            if self.grid[ni][nj] == 1:
                area += self._dfs(ni, nj)
        return area
    
    def _get_valid_next(self, i, j):
        m, n = len(self.grid), len(self.grid[0])
        res = []
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < m and 0 <= nj < n:
                res.append((ni, nj))
        return res
