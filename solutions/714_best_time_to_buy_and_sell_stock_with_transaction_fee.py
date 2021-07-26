class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
    	"""DP.
    	"""
        a, b = 0, -prices[0]
        for price in prices[1:]:
            a, b = max(a, b + price - fee), max(b, a - price)
        return max(a, b)
