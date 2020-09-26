class Solution:
    def fixedPoint(self, A: List[int]) -> int:
    	"""Binary search.

    	Running time: O(nlogn) where n is the length of A.
    	"""
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] >= m:
                r = m
            else:
                l = m + 1
        return l if A[l] == l else -1
