class Solution:
    def toGoatLatin(self, S: str) -> str:
    	"""String.

    	Running time: O(n) where n is the length of S.
    	"""
        words = S.split(' ')
        latin = []
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for i, w in enumerate(words):
            if w[0] in vowels:
                latin.append(w + 'ma' + 'a' * (i + 1))
            else:
                latin.append(w[1:] + w[0] + 'ma' + 'a' * (i + 1))
        return ' '.join(latin)
            