class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Two pointers

        Running Time: O(lt) where lt is the length of string t.
        """
        ls, lt = len(s), len(t)

        if not s: 
            return True
        if ls > lt:
            return False
        
        ps, pt = 0, 0
        while ps < ls and pt < lt:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        
        return ps == ls
