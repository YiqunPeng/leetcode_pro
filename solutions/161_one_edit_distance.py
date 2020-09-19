class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """String

        Running time: O(n) where n is the length of s.
        """
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t) and s[ps] == t[pt]:
            ps += 1
            pt += 1
            
        s = s[ps:]
        t = t[pt:]
        
        if not s and not t:
            return False
        
        if s[1:] == t or s == t[1:] or s[1:] == t[1:]:
            return True
        
        return False