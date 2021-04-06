class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        cubes = 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cubes += grid[i][j]
                cnt += max(0, grid[i][j] - 1)
                if i + 1 < len(grid):
                    cnt += min(grid[i][j], grid[i+1][j])
                if j + 1 < len(grid[0]):
                    cnt += min(grid[i][j], grid[i][j+1])
        return 6 * cubes - 2 * cnt
