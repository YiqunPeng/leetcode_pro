class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """Bit Manipulation.

        Running time: O(logn).
        """
        p = n % 2
        n //= 2
        
        while n:
            r = n % 2
            if p == r:
                return False
            p = r
            n //= 2
            
        return True
     