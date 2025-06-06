class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """DP

        Running Time: O(n^2) where n is the length of nums.
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)