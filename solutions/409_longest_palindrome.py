class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        m = 1
        res = 0
        for k, v in c.items():
            if m and v % 2 == 1:
                res += 1
                m = 0
            res += v // 2 * 2
        return res
