class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	"""Array.

    	Running time: O(n) where n == len(nums).
    	"""
        if not nums:
            return 0
        p = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                p += 1
                nums[p] = nums[i]
        return p + 1
