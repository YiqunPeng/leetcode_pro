class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """String.

        Running time: O(n) where n is the length of s.
        """
        if not s:
            return 0
        
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1
        
        if p < 0:
            return 0
        
        op = p
        while p >= 0 and s[p] != ' ':
            p -= 1
        
        return op - p