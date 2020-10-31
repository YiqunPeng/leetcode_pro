class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    	"""String.
    	"""
        words = sentence.split(' ')
        n = len(searchWord)
        for i, s in enumerate(words):
            if s[:n] == searchWord:
                return i + 1
        return -1
