class Solution:
    def findDerangement(self, n: int) -> int:
    	"""DP.

    	Running time: O(n).
    	"""
        mod = 10 ** 9 + 7
        
        if n == 1:
            return 0
        
        prev, curr = 0, 1
        
        for i in range(3, n + 1):
            prev, curr = curr, ((i - 1) * (prev + curr)) % mod
        
        return curr