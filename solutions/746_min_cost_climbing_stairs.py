class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    	"""DP.

    	Running time: O(n) where n is the length of cost.
    	"""
        n = len(cost)
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
            
        return min(dp[-1], dp[-2])