class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total = 0
        rotten = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    if grid[i][j] == 2:
                        rotten.append((i, j))
                    total += 1
        if total == 0:
            return 0
        rotten_cnt = len(rotten)
        time = 0
        while rotten:
            if rotten_cnt == total:
                return time
            for k in range(len(rotten)):
                i, j = rotten.popleft()
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        rotten.append((ni, nj))
            time += 1
            rotten_cnt += len(rotten)
        return -1
