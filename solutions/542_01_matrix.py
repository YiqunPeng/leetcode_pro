class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j, 0))
                else:
                    matrix[i][j] = float('inf')
        while q:
            i, j, d = q.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == float('inf'):
                    matrix[ni][nj] = d + 1
                    q.append((ni, nj, d + 1))
        return matrix
