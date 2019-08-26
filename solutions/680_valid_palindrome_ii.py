class Solution:
    def validPalindrome(self, s: str) -> bool:
    	"""String.

		Running time: O(n) where n is the length of s.
    	"""
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
            l += 1
            r -= 1
        return True