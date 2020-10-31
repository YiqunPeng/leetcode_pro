class Solution:
    def arrangeWords(self, text: str) -> str:
    	"""String.
    	"""
        text = chr(ord(text[0])-ord('A')+ord('a')) + text[1:]
        words = text.split(' ')
        words.sort(key=len)
        res = ' '.join(words)
        return chr(ord(res[0])-ord('a')+ord('A')) + res[1:]
