class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        """DP.

        Running time: O(Nmn).
        """
        if N == 0:
            return 0
        
        x, y = i, j
        mod = 10 ** 9 + 7
        
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i - 1 < 0:
                    dp[i][j] += 1
                if i + 1 >= m:
                    dp[i][j] += 1
                if j - 1 < 0:
                    dp[i][j] += 1
                if j + 1 >= n:
                    dp[i][j] += 1
        res = dp[x][y]
        
        for k in range(1, N):
            ndp = [[0] * n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= ni < m and 0 <= nj < n:
                            ndp[i][j] = (ndp[i][j] + dp[ni][nj]) % mod
            dp = ndp
            res = (res + dp[x][y]) % mod
            
        return res
