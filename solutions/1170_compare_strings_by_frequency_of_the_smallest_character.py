class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        fw = sorted([self._get_f(w) for w in words])
        return [self._query(fw, q) for q in queries]
        
    def _get_f(self, w):
        """Running time: O(n) where n is the length of w.
        """
        c = w[0]
        f = 1
        for i in w[1:]:
            if i == c:
                f += 1
            elif i < c:
                f = 1
                c = i
        return f
    
    def _query(self, fw, q):
        fq = self._get_f(q)
        return self._search(fw, fq)
    
    def _search(self, fw, fq):
        """Binary search.

        Running time: O(klogk) where k is the length of fw.
        """
        l, r = 0, len(fw) - 1
        while l <= r:
            m = (l + r) // 2
            if fw[m] <= fq:
                l = m + 1
            else:
                r = m - 1
        return len(fw) - l
               