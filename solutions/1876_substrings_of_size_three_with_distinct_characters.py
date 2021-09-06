class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        d = Counter(s[:2])
        res = 0
        for i in range(2, len(s)):
            if i - 3 >= 0:
                d[s[i-3]] -= 1
                if d[s[i-3]] == 0:
                    d.pop(s[i-3])
            d[s[i]] += 1
            if len(d) == 3:
                res += 1
        return res
