class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """Hash table.

        Running time: O(n) where n is the length of word.
        """
        d = {keyboard[i]:i for i in range(26)}
        res = 0
        p = 0
        for w in word:
            res += abs(d[w] - p)
            p = d[w]
        return res
