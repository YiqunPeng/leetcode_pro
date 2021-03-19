class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        q = deque([(0, 0, 1)])
        v = set([(0, 0)])
        while q:
            i, j, s = q.popleft()
            if i == j == len(grid) - 1:
                return s
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in v and grid[ni][nj] == 0:
                    v.add((ni, nj))
                    q.append((ni, nj, s + 1))
        return -1
