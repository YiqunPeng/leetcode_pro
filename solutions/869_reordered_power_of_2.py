class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        d = set()
        cn = self._get_frequence(n)
        k = 1
        while k <= 10 ** 9:
            if cn == self._get_frequence(k):
                return True
            k = k << 1
        return False
    
    def _get_frequence(self, a):
        c = Counter(str(a))
        return tuple((k, c[k]) for k in sorted(c))
