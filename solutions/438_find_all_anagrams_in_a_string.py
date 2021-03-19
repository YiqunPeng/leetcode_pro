class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Sliding window.
        """
        res = []
        cp = Counter(p)
        c = Counter(s[:len(p)])
        if c == cp:
            res.append(0)
        for i in range(1, len(s) - len(p) + 1):
            c[s[i+len(p)-1]] = c.get(s[i+len(p)-1], 0) + 1
            c[s[i-1]] -= 1
            if c[s[i-1]] == 0:
                c.pop(s[i-1])
            if c == cp:
                res.append(i)
        return res
