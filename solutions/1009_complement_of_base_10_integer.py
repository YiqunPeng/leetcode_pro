class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        b = []
        while N != 0:
            b.append(1 - N % 2)
            N //= 2
        res = 0
        for i in range(len(b)):
            res += b[i] * 2 ** i
        return res