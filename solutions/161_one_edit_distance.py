class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """String

        Running time: O(n) where n is the length of s.
        """
        if len(s) > len(t):
            s, t = t, s
        for i in range(len(s)):
            if s[i] != t[i]:
                v = i
                break
        else:
            if len(s) == len(t):
                return False
            else:
                return len(t) - len(s) == 1
        if len(s) == len(t):
            return s[v+1:] == t[v+1:]
        else:
            return s[v:] == t[v+1:]