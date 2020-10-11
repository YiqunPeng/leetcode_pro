class Solution:
    def toLowerCase(self, str: str) -> str:
    	"""String.

    	Running time: O(n) where n == len(str).
    	"""
        d = ord('A') - ord('a')
        s = list(str)
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z':
                s[i] = chr(ord(s[i]) - d)
        return ''.join(s)
