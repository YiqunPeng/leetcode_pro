from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    	"""Hash table.

    	Running time: O(n) where n is the length of target.
    	"""
        return Counter(target) == Counter(arr)
