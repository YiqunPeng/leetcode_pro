class Solution:
    def isPalindrome(self, s: str) -> bool:
        """String.

        Running time: O(n) where n == len(s).
        """
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
