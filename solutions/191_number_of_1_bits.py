class Solution(object):
    def hammingWeight(self, n):
        """Bit manipulation.

        Running time: O(logn).
        """
        ret = 0
        
        while n:
            if n & 1 == 1:
                ret += 1
            n = n >> 1
            
        return ret