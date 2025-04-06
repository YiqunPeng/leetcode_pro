class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '1':
                grid[ni][nj] = '0'
                self.dfs(grid, ni, nj)