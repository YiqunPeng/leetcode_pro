class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """Hash map.

        Running time: O(w * p) where w == len(words) and p == len(pattern).
        """
        res = []
        for w in words:
            if self._match(w, pattern):
                res.append(w)
        return res
    
    def _match(self, w, p):
        m = {}
        mapped = set()
        for i in range(len(w)):
            if p[i] not in m:
                if w[i] in mapped:
                    return False
                m[p[i]] = w[i]
                mapped.add(w[i])
            else:
                if m[p[i]] != w[i]:
                    return False
        return True
