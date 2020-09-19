class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        """Bit manipulation.

        Running time: O(R-L).
        """
        def count_bits(n):
            c = 0
            while n != 0:
                if n % 2 == 1:
                    c += 1
                n //= 2
            return c
        
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        res = 0
        for i in range(L, R + 1):
            if count_bits(i) in primes:
                res += 1
        return res
                