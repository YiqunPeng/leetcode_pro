from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """Hash table.

        Running time: O(n) where n is the lenght of A.
        """
        d = Counter(A[0])
        for a in A[1:]:
            da = Counter(a)
            for k, v in d.items():
                if k not in da:
                    d[k] = 0
                else:
                    d[k] = min(v, da[k])
        res = []
        for k, v in d.items():
            res.extend([k] * v)
        return res
