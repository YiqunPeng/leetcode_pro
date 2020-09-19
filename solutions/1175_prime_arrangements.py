class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        """Math.

        Running time: O(n).
        """
        def is_prime(num):
            if num == 1:
                return 0
            if num % 2 == 0 and num != 2:
                return 0
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return 0
            return 1
        
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)
        
        mod = 10 ** 9 + 7
        
        primes = 0
        for i in range(1, n + 1):
            primes += is_prime(i)
                    
        return ((factorial(primes) % mod) * (factorial(n - primes) % mod)) % mod
            