class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of position.
    	"""
        o, e = 0, 0
        for p in position:
            if p % 2 == 0:
                e += 1
            else:
                o += 1
        return min(e, o)
