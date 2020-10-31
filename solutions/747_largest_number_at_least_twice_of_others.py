class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """Two pointers.

        Running time: O(n) where n is the length of nums.
        """
        if len(nums) == 1:
            return 0
        f, s = 0, 1
        if nums[f] < nums[s]:
            f, s = s, f
        for i in range(2, len(nums)):
            if nums[i] >= nums[f]:
                s, f = f, i
            elif nums[i] > nums[s]:
                s = i
        return f if nums[f] >= nums[s] * 2 else -1
