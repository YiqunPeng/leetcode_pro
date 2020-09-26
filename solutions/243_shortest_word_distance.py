class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        """Running Time: O(n) where n is the length of words.
        """
        w = None
        p = 0
        res = len(words)
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if w is None:
                    w = words[i]
                    p = i
                elif w == words[i]:
                    p = i
                else:
                    w = words[i]
                    res = min(res, i - p)
                    p = i
        return res                 
