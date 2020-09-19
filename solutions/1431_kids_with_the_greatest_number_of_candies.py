class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    	"""Array.

    	Running time: O(n) where n is the length of candies.
    	"""
        n = len(candies)
        res = [False] * n
        max_v = max(candies)
        for i in range(n):
            if candies[i] + extraCandies >= max_v:
                res[i] = True
        return res
