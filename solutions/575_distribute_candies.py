class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
    	"""Hash set.
    	"""
        s = set(candyType)
        if len(s) > len(candyType) // 2:
            return len(candyType) // 2
        else:
            return len(s)
