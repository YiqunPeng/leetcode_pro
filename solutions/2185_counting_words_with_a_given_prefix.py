class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(word) >= len(pref) and word[0:len(pref)] == pref:
                res += 1
        return res