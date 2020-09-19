class Solution:
    def rob(self, nums: List[int]) -> int:
    	"""DP.

    	Running time: O(n) where n is the length of nums.
    	"""
        if not nums:
            return 0
        
        dp = [[0, 0] for i in range(len(nums))]
        dp[0][1] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + nums[i]
            
        return max(dp[-1])
