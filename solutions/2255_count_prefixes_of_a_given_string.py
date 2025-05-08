class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for w in words: 
            if s[:len(w)] == w:
                res += 1
        return res