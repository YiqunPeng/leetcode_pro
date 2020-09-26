class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        n = len(nums)
        l, r = [0] * n, [0] * n
        for i in range(1, n):
            if nums[i-1] == 1:
                l[i] = l[i-1] + 1
        for i in range(n-2, -1, -1):
            if nums[i+1] == 1:
                r[i] = r[i+1] + 1
        res = 0
        for i in range(n):
            res = max(res, l[i] + r[i])
        return res
