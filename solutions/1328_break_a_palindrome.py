class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
    	"""String.

    	Running time: O(n) where n == len(palindrome).
    	"""
        n = len(palindrome)
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        if len(palindrome) > 1:
            return palindrome[:-1] + 'b'
        else:
            return ""
