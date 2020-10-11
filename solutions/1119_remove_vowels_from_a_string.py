class Solution:
    def removeVowels(self, S: str) -> str:
    	"""String.

    	Running time: O(n) where n is the length of S.
    	"""
        p = 0
        v = set(['a', 'e', 'i', 'o', 'u'])
        S = list(S)
        for i in range(len(S)):
            if S[i] not in v:
                S[p] = S[i]
                p += 1
        return ''.join(S[:p])
