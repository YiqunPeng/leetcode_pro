class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
    	"""Hash table

    	Running Time: O(c) where c is total amount of char in words.
    	"""
        s = set()
        for w in words:
            c = self._encode(w, codes)
            s.add(c)
        return len(s)

    def _encode(self, word, codes):
        res = ''
        for w in word:
            res += codes[ord(w) - ord('a')]
        return res
