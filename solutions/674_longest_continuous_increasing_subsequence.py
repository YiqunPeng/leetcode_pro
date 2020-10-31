class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        if not nums:
            return 0
        c = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c += 1
            else:
                res = max(res, c)
                c = 1
        return max(res, c)
