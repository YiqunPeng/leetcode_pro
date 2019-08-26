class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    	"""Math.

		Running time: O(n) where n is the length of nums.
    	"""
        s = sum(nums)
        
        t = 0
        for i, num in enumerate(nums):
            if t == (s - num) / 2:
                return i
            t += num
        
        return -1