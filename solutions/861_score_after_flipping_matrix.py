class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        res = 0
        for j in range(n):
            c = 0
            for i in range(m):
                c += grid[i][j]
            if c > m // 2:
                res += 2 ** (n - 1 - j) * c
            else:
                res += 2 ** (n - 1 - j) * (m - c)
        return res
