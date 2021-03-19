class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """BFS.
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        res = -1
        if not q or len(q) == m * n:
            return -1
        while q:
            for k in range(len(q)):
                i, j = q.popleft()
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append((ni, nj))
            res += 1
        return res
