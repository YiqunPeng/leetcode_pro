class Solution:
    
    def __init__(self):
        self.total_d = defaultdict(int)
        self.total_c = defaultdict(int)
        self.buildings = []
        
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """BFS.
        """
        if not grid:
            return -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.buildings.append((i, j))
        for i, j in self.buildings:
            if len(self.buildings) > self._bfs(grid, i, j):
                return -1
        res = float('inf')
        for k, v in self.total_d.items():
            if self.total_c[k] == len(self.buildings):
                res = min(res, v)
        return res if res != float('inf') else -1
    
    def _bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        visited = set([(i, j)])
        q = deque([(0, i, j)])
        bcnt = 1
        while q:
            d, i, j = q.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    if grid[ni][nj] == 0:
                        q.append((d + 1, ni, nj))
                        self.total_d[(ni, nj)] += d + 1
                        self.total_c[(ni, nj)] += 1
                    elif grid[ni][nj] == 1:
                        bcnt += 1
        return bcnt
