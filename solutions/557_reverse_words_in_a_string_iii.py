class Solution:
    def reverseWords(self, s: str) -> str:
    	"""String.

		Running time: O(n) where n is the length of s.
    	"""
        words = s.split(' ')
        return ' '.join([word[::-1] for word in words])