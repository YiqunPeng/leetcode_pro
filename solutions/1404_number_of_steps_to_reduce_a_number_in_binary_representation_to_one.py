class Solution:
    def numSteps(self, s: str) -> int:
    	"""String.

    	Running time: O(n) where n == len(s).
    	"""
        carry, res = 0, 0
        for i in s[:0:-1]:
            if int(i) + carry == 1:
                res += 2
                carry = 1
            else:
                res += 1
        return res + carry
