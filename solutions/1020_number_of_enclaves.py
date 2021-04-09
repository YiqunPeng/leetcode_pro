class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            if grid[i][0] == 1:
                grid[i][0] = 0
                self._dfs(grid, i, 0)
            if grid[i][len(grid[0])-1] == 1:
                grid[i][len(grid[i])-1] = 0
                self._dfs(grid, i, len(grid[0])-1)
        for j in range(len(grid[0])):
            if grid[0][j] == 1:
                grid[0][j] = 0
                self._dfs(grid, 0, j)
            if grid[len(grid)-1][j] == 1:
                grid[len(grid)-1][j] = 0
                self._dfs(grid, len(grid)-1, j)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += 1
        return res
    
    def _dfs(self, grid, i, j):
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                grid[ni][nj] = 0
                self._dfs(grid, ni, nj)
