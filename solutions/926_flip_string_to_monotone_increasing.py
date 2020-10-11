class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        """Array.

        Running time: O(n) where n is the length of S.
        """
        n = len(S)
        res = 0
        ones, zeros = 0, 0
        for i in range(n):
            if S[i] == '0' and ones == 0:
                continue
            if S[i] == '1':
                ones += 1
            else:
                zeros += 1
            if zeros > ones:
                res += ones
                ones = 0
                zeros = 0
        return res + zeros
