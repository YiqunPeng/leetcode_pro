class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """String.

        Running time: O(n) where n == len(abbr).
        """
        v = p = 0
        for i in abbr:
            if i.isalpha():
                p += v
                v = 0
                if p >= len(word) or word[p] != i:
                    return False
                else:
                    p += 1
            else:
                if not v and int(i) == 0:
                    return False
                else:
                    v = v * 10 + int(i)
        return p + v == len(word)
