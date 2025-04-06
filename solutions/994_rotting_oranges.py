class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        f = 0
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    f += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        if f == 0:
            return 0
        
        while q:
            i, j, m = q.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                    f -= 1
                    if f == 0:
                        return m + 1
                    grid[ni][nj] = 2
                    q.append((ni, nj, m + 1))
        
        return -1