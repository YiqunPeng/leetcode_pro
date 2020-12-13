class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """String.

        Running time: O(n) where n is the length of s.
        """
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1
        if p >= 0:
            r = p
        else:
            return 0
        while p >= 0 and s[p] != ' ':
            p -= 1
        return r - p
