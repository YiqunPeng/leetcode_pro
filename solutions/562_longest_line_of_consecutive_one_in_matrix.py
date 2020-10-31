class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        """DP.

        Running time: O(m * n) where m == len(M) and n == len(M[0]).
        """
        if not M:
            return 0
        res = 0
        d = {}
        m, n = len(M), len(M[0])
        if M[0][0] == 0:
            d[(0, 0)] = [0, 0, 0, 0]
        else:
            d[(0, 0)] = [1, 1, 1, 1]
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    d[(i, j)] = [1, 1, 1, 1]
                    if i - 1 >= 0:
                        d[(i, j)][0] = d[(i-1, j)][0] + 1
                    if j - 1 >= 0:
                        d[(i, j)][1] = d[(i, j-1)][1] + 1
                    if i - 1 >= 0 and j - 1 >= 0:
                        d[(i, j)][2] = d[(i-1, j-1)][2] + 1
                    if i - 1 >= 0 and j + 1 < n:
                        d[(i, j)][3] = d[(i-1, j+1)][3] + 1
                    res = max(res, max(d[(i, j)]))
                else:
                    d[(i, j)] = [0, 0, 0, 0]
        return res
