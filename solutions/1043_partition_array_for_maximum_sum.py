class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_v = 0
            for j in range(1, min(i + 1, k + 1)):
                max_v = max(max_v, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + max_v * j)
        return dp[-1]
