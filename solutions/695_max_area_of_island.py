class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, self._get_area(i, j, grid))
        return res
    
    def _get_area(self, i, j, grid):
        grid[i][j] = 0
        area = 1
        for ni, nj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                area += self._get_area(ni, nj, grid)
        return area
                