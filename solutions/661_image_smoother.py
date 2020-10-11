class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        """Array.

        Running time: O(m * n) where m and n are the size of M.
        """
        m, n = len(M), len(M[0])
        res = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = self._smooth(M, i, j)
        return res
    
    def _smooth(self, M, r, c):
        m, n = len(M), len(M[0])
        s = 0
        rl, rr = max(0, r - 1), min(r + 2, m)
        cl, cr = max(0, c - 1), min(c + 2, n)
        for i in range(rl, rr):
            for j in range(cl, cr):
                s += M[i][j]               
        return s // ((rr - rl) * (cr - cl))
