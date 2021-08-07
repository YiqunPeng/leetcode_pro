class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float('inf')] * n
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])-1, -1, -1):
                if j - 1 >= 0:
                    dp[j] = min(dp[j], dp[j-1])
                dp[j] += triangle[i][j]
        return min(dp)
