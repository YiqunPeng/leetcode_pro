class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Hash Table.

        Running time: O(n) where n is the length of s.
        """
        d = {}
        
        ret = 0
        l, r = 0, 0
        
        while r < len(s):
            if s[r] in d and d[s[r]] >= l:
                ret = max(ret, r - l)
                l = d[s[r]] + 1
            
            d[s[r]] = r
            r += 1
        
        return max(ret, r - l)   
        