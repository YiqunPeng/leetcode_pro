class Solution:
    def rob(self, nums: List[int]) -> int:
        """DP.

        Running time: O(n) where n is the length of nums.
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return max(nums)
        
        dp = [[0, 0] for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + nums[i]
            
        res = max(dp[-1])
        
        dp = [[0, 0] for i in range(len(nums))]
        dp[0][1] = nums[0]
        
        for i in range(1, len(nums) - 1):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + nums[i]
        
        return max(res, max(dp[-2]))
