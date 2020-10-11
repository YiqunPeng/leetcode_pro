class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n is the length of A.
    	"""
        b = A[0] - 1
        res = -1
        for i in range(1, len(A)):
            res = max(res, A[i] + b)
            b = max(b - 1, A[i] - 1)
        return res
