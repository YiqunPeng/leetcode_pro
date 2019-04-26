class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        """Running Time: O(n) where n is the length of words.
        """
        s = word1 == word2
        i0 = -1
        d = sys.maxsize
        
        for i, w in enumerate(words):
            if w == word1 or w == word2:
                if i0 != -1 and (s or (not s and words[i] != words[i0])):
                    d = min(d, i - i0)
                i0 = i
        
        return d
