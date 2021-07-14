class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        fresh = 0
        m, n = len(grid), len(grid[0])
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))
        res = 0
        while rotten:
            new_rotten = []
            for i, j in rotten:
                for (ni, nj) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        new_rotten.append((ni, nj))
            rotten = new_rotten
            if rotten:
                res += 1
        if fresh == 0:
            return res
        else:
            return -1