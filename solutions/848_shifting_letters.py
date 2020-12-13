class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        """String.

        Running time: O(n) where n == len(shifts).
        """
        orda = ord('a')
        n = len(shifts)
        suf = shifts
        suf[-1] %= 26
        for i in range(n - 2, -1, -1):
            suf[i] = (suf[i] + suf[i+1]) % 26
        res = [''] * n
        for i in range(n):
            res[i] = chr(orda + (ord(S[i]) - orda + suf[i]) % 26)
        return ''.join(res)
