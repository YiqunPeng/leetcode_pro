class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """Hash table.

        Running time: O(n) where n is the length of word.
        """
        d = {}
        for i, key in enumerate(keyboard):
            d[key] = i
            
        ret = 0
        p = 0
        
        for c in word:
            idx = d[c]
            ret += abs(idx - p)
            p = idx
        
        return ret