class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n - 1) & n == 0 and (n & 0x555555555) == n
