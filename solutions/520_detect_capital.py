class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    	"""String.
    	"""
        if word[0].isupper():
            return all(i.isupper() for i in word[1:]) or all(i.islower() for i in word[1:])
        else:
            return all(i.islower() for i in word[1:])
