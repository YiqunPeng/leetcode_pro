class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        ocolor = grid[r0][c0]
        visited = set()
        visited.add((r0, c0))
        updates = set()
        self._dfs(grid, r0, c0, ocolor, visited, updates)
        for r, c in updates:
            grid[r][c] = color
        return grid
    
    def _dfs(self, grid, r, c, oldc, v, updates):
        m, n = len(grid), len(grid[0])
        if r in [0, m - 1] or c in [0, n - 1]:
            updates.add((r, c))
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == oldc and (nr, nc) not in v:
                    v.add((nr, nc))
                    self._dfs(grid, nr, nc, oldc, v, updates)
                if grid[nr][nc] != oldc:
                    updates.add((r, c))
