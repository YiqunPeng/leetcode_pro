class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concat = ''
        for w in words:
            if len(concat) + len(w) <= len(s):
                concat += w
            else:
                break
        return concat == s