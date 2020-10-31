class Solution:
    def printVertically(self, s: str) -> List[str]:
        """String.
        """
        words = s.split(' ')
        res = []
        for i, w in enumerate(words):
            k = len(res)
            for j in range(k):
                if j < len(w):
                    res[j] += w[j]
                else:
                    res[j] += ' '
            while k < len(w):
                res.append(' ' * i + w[k])
                k += 1
        return [i.rstrip() for i in res]
