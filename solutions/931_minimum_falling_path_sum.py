class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for i in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(n):
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1])
                dp[i][j] = min(dp[i][j], dp[i-1][j]) + matrix[i][j]
        return min(dp[-1])
