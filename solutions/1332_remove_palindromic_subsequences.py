class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        if not s:
            return 0
        elif self._is_palindromic(s):
            return 1
        else:
            return 2
        
    def _is_palindromic(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
