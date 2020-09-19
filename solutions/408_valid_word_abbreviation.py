class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """String.

        Running time: O(n) where n is length of abbr.
        """
        v = 0
        p = 0
        
        for c in abbr:
            if c in string.digits:
                if int(c) == 0 and v == 0:
                    return False
                v = v * 10 + int(c)
            else:
                p += v
                v = 0
                if p < len(word) and word[p] == c:
                    p += 1
                else:
                    return False
                
        return p + v == len(word)