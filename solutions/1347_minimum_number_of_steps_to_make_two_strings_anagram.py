class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """Hash table.

        Running time: O(n) where n is the length of s.
        """
        c_s = collections.Counter(s)
        c_t = collections.Counter(t)
        
        res = len(s)
        for k, v in cs.items():
            if k in ct:
                res -= min(v, ct[k])
        return res
