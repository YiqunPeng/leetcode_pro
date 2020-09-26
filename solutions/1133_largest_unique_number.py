from collections import Counter

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
    	"""Hash table.

    	Running time: O(n) where n is the length of A.
    	"""
        ca = Counter(A)
        mx = -1
        for k, v in ca.items():
            if v == 1 and mx < k:
                mx = k
        return mx
