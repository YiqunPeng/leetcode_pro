class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        mark = [[0] * n for i in range(m)]
        self._mark_pacific(mark, matrix)
        self._mark_atlantic(mark, matrix)
        res = []
        for i in range(m):
            for j in range(n):
                if mark[i][j] == 2:
                    res.append([i, j])
        return res
    
    def _mark_pacific(self, mark, matrix):
        v = set()
        q = deque()
        for i in range(1, len(mark)):
            v.add((i, 0))
            q.append((i, 0))
        for j in range(len(mark[0])):
            v.add((0, j))
            q.append((0, j))
        while q:
            i, j = q.popleft()
            mark[i][j] += 1
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < len(mark) and 0 <= nj < len(mark[0]) and (ni, nj) not in v and matrix[ni][nj] >= matrix[i][j]:
                    q.append((ni, nj))
                    v.add((ni, nj))
    
    def _mark_atlantic(self, mark, matrix):
        v = set()
        q = deque()
        for i in range(len(mark)-1):
            v.add((i, len(mark[0])-1))
            q.append((i, len(mark[0])-1))
        for j in range(len(mark[0])):
            v.add((len(mark)-1, j))
            q.append((len(mark)-1, j))
        while q:
            i, j = q.popleft()
            mark[i][j] += 1
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < len(mark) and 0 <= nj < len(mark[0]) and (ni, nj) not in v and matrix[ni][nj] >= matrix[i][j]:
                    q.append((ni, nj))
                    v.add((ni, nj))
