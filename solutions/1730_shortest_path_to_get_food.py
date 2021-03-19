class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        x, y = self._find_start(grid)
        q = deque([(x, y, 0)])
        seen = set([(x, y)])
        while q:
            x, y, p = q.popleft()
            if grid[x][y] == '#':
                return p
            for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] != 'X' and (dx, dy) not in seen:
                    seen.add((dx, dy))
                    q.append((dx, dy, p + 1))
        return -1
    
    def _find_start(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    return i, j
