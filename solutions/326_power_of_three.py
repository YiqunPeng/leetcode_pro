class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_v = 1162261467
        return n > 0 and max_v % n == 0
