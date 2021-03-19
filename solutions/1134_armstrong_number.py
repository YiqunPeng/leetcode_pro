class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        k = len(s)
        v = 0
        for c in s:
            c = int(c)
            v += c ** k
        return v == n
