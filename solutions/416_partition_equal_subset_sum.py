class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        half = s // 2
        n = len(nums)
        dp = [False] * (half + 1)
        dp[0] = True
        for i in range(n):
            for j in range(half, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]
            if dp[half]:
                return True
        return False
