class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        return [self._dfs(i, 0, grid) for i in range(len(grid[0]))]
    
    def _dfs(self, i, row, grid):
        if row == len(grid):
            return i
        if grid[row][i] == 1:
            if i + 1 == len(grid[0]) or grid[row][i+1] == -1:
                return -1
            return self._dfs(i+1, row+1, grid)
        else:
            if i == 0 or grid[row][i-1] == 1:
                return -1
            return self._dfs(i-1, row+1, grid)
