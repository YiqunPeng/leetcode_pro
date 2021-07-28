class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = ''
        for c in order:
            if c in counter:
                res = res + c * counter[c]
                counter.pop(c)
        for k in counter:
            res = res + k * counter[k]
        return res
