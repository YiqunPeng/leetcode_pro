class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        cell = {
            1: (0, 1, 0, 1),
            2: (1, 0, 1, 0),
            3: (0, 0, 1, 1),
            4: (0, 1, 1, 0),
            5: (1, 0, 0, 1),
            6: (1, 1, 0, 0)
        }
        m, n = len(grid), len(grid[0])
        visited = set([(0, 0)])
        q = deque([(0, 0)])
        while q:
            i, j = q.popleft()
            if i == m - 1 and j == n - 1:
                return True
            t = cell[grid[i][j]]
            if t[0] == 1:
                if i > 0 and cell[grid[i-1][j]][2] == 1 and (i-1, j) not in visited:
                    visited.add((i-1, j))
                    q.append((i-1, j))
            if t[1] == 1:
                if j+1 < n and cell[grid[i][j+1]][3] == 1 and (i, j+1) not in visited:
                    visited.add((i, j+1))
                    q.append((i, j+1))
            if t[2] == 1:
                if i+1 < m and cell[grid[i+1][j]][0] == 1 and (i+1, j) not in visited:
                    visited.add((i+1, j))
                    q.append((i+1, j))
            if t[3] == 1:
                if j > 0 and cell[grid[i][j-1]][1] == 1 and (i, j-1) not in visited:
                    visited.add((i, j-1))
                    q.append((i, j-1))
        return False
