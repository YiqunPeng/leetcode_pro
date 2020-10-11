class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    	"""Math.

    	Running time: O(k) where k is the number of ants.
    	"""
        return max(left + [n - i for i in right])
