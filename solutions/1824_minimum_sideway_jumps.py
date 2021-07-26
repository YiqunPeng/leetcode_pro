class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [0, 1, 0, 1]
        for i in range(1, n):
            dp[obstacles[i]] = float('inf')
            minj = min(dp[1:])
            for l in range(1, 4):
                dp[l] = min(dp[l], minj + 1)
            dp[obstacles[i]] = float('inf')
        return min(dp[1:])
