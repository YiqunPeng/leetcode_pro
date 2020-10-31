class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if self._search(m, S):
                l = m + 1
            else:
                r = m - 1
        return l - 1
    
    def _search(self, length, S):
        seen = set()
        for i in range(0, len(S) - length + 1):
            if S[i:i+length] in seen:
                return True
            seen.add(S[i:i+length])
        return False
