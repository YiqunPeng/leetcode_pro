class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        c, f = {}, {}
        de = 0
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] not in f:
                f[nums[i]] = i
            c[nums[i]] = c.get(nums[i], 0) + 1
            if c[nums[i]] > de:
                de = c[nums[i]]
                res = i - f[nums[i]] + 1
            elif c[nums[i]] == de:
                res = min(res, i - f[nums[i]] + 1)
        return res
