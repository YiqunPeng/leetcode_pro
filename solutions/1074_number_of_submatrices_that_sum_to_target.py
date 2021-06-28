class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        res = 0
        for i in range(n):
            for j in range(i, n):
                d = defaultdict(int)
                d[0] = 1
                s = 0
                for k in range(m):
                    s += matrix[k][j] - (matrix[k][i-1] if i else 0)
                    res += d[s - target]
                    d[s] += 1
        return res
