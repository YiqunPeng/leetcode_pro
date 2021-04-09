class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    if self._dfs(grid, i, j):
                        res += 1
        return res
    
    def _dfs(self, grid, i, j):
        closed = 0 < i < len(grid) - 1 and 0 < j < len(grid[0]) - 1
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 0:
                grid[ni][nj] = 1
                closed = self._dfs(grid, ni, nj) and closed
        return closed
