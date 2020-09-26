class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n^2) where n is the length of prices.
    	"""
        res = prices
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res
