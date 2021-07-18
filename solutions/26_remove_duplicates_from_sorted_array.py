class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n == len(nums).
    	"""
        l, r = 0, 1
        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1
