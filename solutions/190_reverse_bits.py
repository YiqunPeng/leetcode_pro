class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += (n & 1) * 2 ** (31 - i)
            n >>= 1
        return res