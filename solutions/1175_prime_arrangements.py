class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10 ** 9 + 7
        prime = 0
        for i in range(2, n + 1):
            prime += self._is_prime(i)
        return ((self._factorial(prime) % mod) * (self._factorial(n - prime) % mod)) % mod
    
    def _is_prime(self, num):
        if num % 2 == 0:
            return 1 if num == 2 else 0
        for i in range(3, int(num ** 0.5) + 1):
            if num % i == 0:
                return 0
        return 1
    
    def _factorial(self, n):
        res = 1
        while n > 1:
            res *= n
            n -= 1
        return res
