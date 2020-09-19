class Solution:
    def xorOperation(self, n: int, start: int) -> int:
    	"""Array.

    	Running time: O(n).
    	"""
        res = start
        for i in range(1, n):
            v = start + 2 * i
            res ^= v
        return res
