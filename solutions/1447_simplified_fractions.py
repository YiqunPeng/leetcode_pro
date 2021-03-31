class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if self._gcd(j, i) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
    
    def _gcd(self, a, b):
        return a if b % a == 0 else self._gcd(b % a, a)
