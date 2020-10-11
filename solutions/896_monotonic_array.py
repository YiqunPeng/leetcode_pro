class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
    	"""Array.

    	Running time: O(n) where n is the length of A.
    	"""
        n = len(A)
        inc, dec = True, True
        for i in range(1, n):
            if dec and A[i] > A[i-1]:
                dec = False
            if inc and A[i] < A[i-1]:
                inc = False
        return inc or dec
