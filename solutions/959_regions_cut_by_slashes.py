class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        seen = set()
        res = 0
        for i in range(n):
            for j in range(n):
                if (i, j, 0) not in seen:
                    self._dfs(grid, i, j, 0, seen)
                    res += 1
                if (i, j, 1) not in seen:
                    self._dfs(grid, i, j, 1, seen)
                    res += 1
        return res
    
    def _dfs(self, grid, i, j, a, seen):
        if (i, j, a) in seen:
            return
        n = len(grid)
        seen.add((i, j, a))
        if grid[i][j] == ' ':
            if a == 0:
                self._dfs(grid, i, j, 1, seen)
                if i > 0:
                    if grid[i-1][j] in [' ', '/']:
                        self._dfs(grid, i-1, j, 1, seen)
                    else:
                        self._dfs(grid, i-1, j, 0, seen)
                if j > 0:
                    self._dfs(grid, i, j-1, 1, seen)
            else:
                self._dfs(grid, i, j, 0, seen)
                if j + 1 < n:
                    self._dfs(grid, i, j+1, 0, seen)
                if i + 1 < n:
                    if grid[i+1][j] in ['/', ' ']:
                        self._dfs(grid, i+1, j, 0, seen)
                    else:
                        self._dfs(grid, i+1, j, 1, seen)
        elif grid[i][j] == '\\':
            if a == 0:
                if j > 0:
                    self._dfs(grid, i, j-1, 1, seen)
                if i + 1 < n:
                    if grid[i+1][j] in ['/', ' ']:
                        self._dfs(grid, i+1, j, 0, seen)
                    else:
                        self._dfs(grid, i+1, j, 1, seen)                    
            else:
                if j + 1 < n:
                    self._dfs(grid, i, j+1, 0, seen)
                if i > 0:
                    if grid[i-1][j] in [' ', '/']:
                        self._dfs(grid, i-1, j, 1, seen)
                    else:
                        self._dfs(grid, i-1, j, 0, seen)
        else:
            if a == 0:
                if i > 0:
                    if grid[i-1][j] in [' ', '/']:
                        self._dfs(grid, i-1, j, 1, seen)
                    else:
                        self._dfs(grid, i-1, j, 0, seen)
                if j > 0:
                    self._dfs(grid, i, j-1, 1, seen)
            else:
                if j + 1 < n:
                    self._dfs(grid, i, j+1, 0, seen)
                if i + 1 < n:
                    if grid[i+1][j] in ['/', ' ']:
                        self._dfs(grid, i+1, j, 0, seen)
                    else:
                        self._dfs(grid, i+1, j, 1, seen)
