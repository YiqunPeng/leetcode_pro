class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ''
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '-':
                continue
            elif '0' <= s[i] <= '9':
                res += s[i]
                c += 1
            else:
                res += s[i].upper()
                c += 1
            if c == k:
                res += '-'
                c = 0
        if res and res[-1] == '-':
            return res[:-1][::-1]
        else:
            return res[::-1]