class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n == len(nums).
    	"""
        p = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[p-1]:
                p += 1
                nums[p] = nums[i]
        return p + 1
