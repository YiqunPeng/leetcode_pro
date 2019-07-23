class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r, c = [0] * n, [0] * n
        t = 0
        
        for i in range(n):
            for j in range(n):
                t += grid[i][j] > 0
                r[i] = max(r[i], grid[i][j])
                c[j] = max(c[j], grid[i][j])
        
        return t + sum(r + c)
  