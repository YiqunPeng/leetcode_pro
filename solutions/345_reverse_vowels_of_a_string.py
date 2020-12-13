class Solution:
    def reverseVowels(self, s: str) -> str:
        """String.

        Running time: O(n) where n is the length of s.
        """
        v = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        sl = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and sl[l] not in v:
                l += 1
            while l < r and sl[r] not in v:
                r -= 1
            if l < r:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
        return ''.join(sl)
