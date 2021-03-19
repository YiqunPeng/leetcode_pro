class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        res = [[-1] * n for i in range(m)]
        q = deque([(i, j, 0) for i, j in self._get_water_cell(isWater, res)])
        while q:
            i, j, h = q.popleft()
            res[i][j] = h
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n and res[ni][nj] == -1:
                    res[ni][nj] = h + 1
                    q.append((ni, nj, h + 1))
        return res
    
    def _get_water_cell(self, isWater, res):
        cells = []
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    cells.append((i, j))
                    res[i][j] = 0
        return cells
