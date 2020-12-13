class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """Two pointers.

        Running time: O(n) where n is the length of s.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l, r = 0, 0
        while l < len(s):
            while r < len(s) and s[r] != ' ':
                r += 1
            t = r - 1
            while l < t:
                s[l], s[t] = s[t], s[l]
                l += 1
                t -= 1
            l, r = r + 1, r + 1
