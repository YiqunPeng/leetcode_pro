class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """Sliding window.

        Running time: O(n) where n == len(s).
        """
        i = 0
        d = collections.defaultdict(int)
        for j in range(len(s)):
            d[s[j]] += 1
            if len(d) > 2:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
        return len(s) - i
