class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        for j in range(n):
            dp[j][j] = piles[j]
            for i in range(j-1, -1, -1):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][-1] > 0
