class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        l, r = 0, 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res += s[start+1:i]
                start = i + 1
        return res
