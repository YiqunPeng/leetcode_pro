class Solution:
    def toGoatLatin(self, S: str) -> str:
    	"""String.

    	Running time: O(n) where n is the length of S.
    	"""
        words = S.split(' ')
        
        for i in range(len(words)):
            if words[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                words[i] = words[i] + 'ma'
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma'
            words[i] = words[i] + 'a' * (i + 1)
        
        return ' '.join(words)
            