class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        s = 0
        p = 1
        for c in n:
            c = int(c)
            s += c
            p *= c
        return p - s
