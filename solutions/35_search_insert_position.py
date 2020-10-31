class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Binary Search

        Running Time: O(n log n) where n is the length of nums.
        """
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
