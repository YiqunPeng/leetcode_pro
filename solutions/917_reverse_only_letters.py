class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        """String.

        Running time: O(n) where n == len(S).
        """
        sl = list(S)
        l, r = 0, len(sl) - 1
        while l < r:
            if sl[l] not in string.ascii_letters:
                l += 1
            elif sl[r] not in string.ascii_letters:
                r -= 1
            else:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
        return ''.join(sl)
