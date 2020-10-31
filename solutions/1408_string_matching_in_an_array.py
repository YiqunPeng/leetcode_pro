class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res = []
        lps = [self._compute_lps(w) for w in words[:-1]]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self._kmp(words[i], words[j], lps[i]):
                    res.append(words[i])
                    break
        return res
    
    def _kmp(self, w, s, lps):
        i, j = 0, 0
        c = 0
        while i < len(s):
            if s[i] == w[j]:
                i += 1
                j += 1
                if j == len(w):
                    return True
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return False
    
    def _compute_lps(self, w):
        n = len(w)
        lps = [0] * n
        i = 1
        p = 0
        while i < n:
            if w[i] == w[p]:
                p += 1
                lps[i] = p
                i += 1
            else:
                if p != 0:
                    p = lps[p-1]
                else:
                    p = 0
                    i += 1
        return lps
