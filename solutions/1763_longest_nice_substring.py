class Solution:
    def longestNiceSubstring(self, s: str) -> str:
    	"""Divide and conquer.
    	"""
        if not s:
            return ""
        sset = set(s)
        for i in range(len(s)):
            if s[i].upper() in sset and s[i].lower() in sset:
                continue
            lsub = self.longestNiceSubstring(s[:i])
            rsub = self.longestNiceSubstring(s[i+1:])
            return lsub if len(lsub) >= len(rsub) else rsub
        return s
