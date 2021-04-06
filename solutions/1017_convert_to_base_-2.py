class Solution:
    def baseNeg2(self, N: int) -> str:
        res = []
        while N != 0:
            res.append(str(N % 2))
            N = -(N >> 1)
        return ''.join(res[::-1] if res else ['0'])
