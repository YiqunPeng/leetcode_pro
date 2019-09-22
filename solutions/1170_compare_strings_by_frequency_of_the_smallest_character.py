class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        """Binary search.

        Running time: O(w + qlogw) where q is the length of queries and w is the length of words.
        """
        def get_frequency(word):
            w = collections.Counter(word)
            for c in string.ascii_lowercase:
                if c in w:
                    return w[c]
        
        def compare(qf, f):
            if qf >= f[0]:
                return 0
            if qf < f[-1]:
                return len(f)
            
            l, r = 0, len(f) - 1
            while l < r:
                m = l + (r - l) // 2
                if f[m-1] > qf >= f[m]:
                    return m
                elif qf < f[m]:
                    l = m + 1
                else:
                    r = m
            return r
        
        f = sorted([get_frequency(word) for word in words], reverse=True)
        return [compare(get_frequency(q), f) for q in queries]
               