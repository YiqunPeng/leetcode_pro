class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """Hash table.

        Running time: O(n) where n is the length of s.
        """
        c_s = collections.Counter(s)
        c_t = collections.Counter(t)
        
        res = 0
        for k, v in c_t.items():
            if k not in c_s:
                res += v
            elif c_s[k] < v:
                res += v - c_s[k]
        
        return res
