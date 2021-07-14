class Solution(object):
    def hammingWeight(self, n):
        """Bit manipulation.

        Running time: O(logn).
        """
        res = 0
        while n != 0:
            if n % 2 == 1:
                res += 1
            n //= 2
        return res
