class Solution:
    def secondHighest(self, s: str) -> int:
        l, sl = -1, -1
        for c in s:
            if '0' <= c <= '9':
                v = int(c)
                if v > l:
                    l, sl = v, l
                elif l > v > sl:
                    sl = v
        return sl
