class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of prices.
    	"""
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
        return res
