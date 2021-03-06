class Solution:
    def numSquares(self, n: int) -> int:
    	"""DP.

    	Running time: O(n^(3/2))
    	"""
        dp = [0]
        
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5)+1)) + 1,
        
        return dp[n]