class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = 0
        d = {}
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            if len(d) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
        return j - i + 1
