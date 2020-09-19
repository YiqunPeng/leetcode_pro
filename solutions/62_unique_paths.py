class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """DP.

        Running time: O(n * m).
        """
        dp = [[0] * n for i in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]