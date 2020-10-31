class Solution:
    def findContestMatch(self, n: int) -> str:
    	"""Recursion.

    	Running time: O(n).
    	"""
        m = [i+1 for i in range(n)]
        while n > 0:
            for i in range(n // 2):
                m[i] = '(' + str(m[i]) + ',' + str(m[n - 1 - i]) + ')'
            n //= 2
        return m[0]
