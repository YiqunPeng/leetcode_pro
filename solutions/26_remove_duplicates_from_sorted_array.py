class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Two pointers.

        Running time: O(n) where n is the length of nums.
        """
        if not nums:
            return 0
        
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        
        return l + 1