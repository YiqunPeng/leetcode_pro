class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        """KMP.
        """
        res = []
        for w in words:
            res.extend(self._kmp(text, w))
        return sorted(res)
    
    def _kmp(self, text, w):
        lps = self._compute_lps(w)
        r = []
        m, n = len(text), len(w)
        i, j = 0, 0
        while i < m:
            if text[i] == w[j]:
                i += 1
                j += 1
                if j == n:
                    r.append([i-n, i-1])
                    j = lps[j-1]
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return r
    
    def _compute_lps(self, w):
        n = len(w)
        lps = [0] * n
        l, i = 0, 1
        while i < n:
            if w[i] == w[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    i += 1
        return lps
