class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    	"""Bit manipulation

		Running time: O(logn)
    	"""
        return n > 0 and n & (n - 1) == 0