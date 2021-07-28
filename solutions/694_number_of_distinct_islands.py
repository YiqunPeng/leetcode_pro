class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands.add(self._bfs(grid, i, j))
        return len(islands)
    
    def _bfs(self, grid, si, sj):
        island = [(0, 0)]
        grid[si][sj] = 0
        q = deque([(si, sj)])
        while q:
            i, j = q.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    island.append((ni - si, nj - sj))
                    q.append((ni, nj))
        return tuple(island)
