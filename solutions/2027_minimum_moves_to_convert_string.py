class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        l = 0
        while l < len(s):
            if s[l] == 'X':
                res += 1
                l += 3
            else:
                l += 1
        return res
