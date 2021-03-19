class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """Hash table.
        """
        res = 0
        d = {0: -1}
        c = 0
        for i, n in enumerate(nums):
            if n == 1:
                c -= 1
            else:
                c += 1
            if c in d:
                res = max(res, i - d[c])
            else:
                d[c] = i
        return res
