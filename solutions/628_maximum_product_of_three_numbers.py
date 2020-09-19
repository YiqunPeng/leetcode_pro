class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
    	"""Math.

    	Running time: O(nlogn) where n is the length of nums.
    	"""
        nums.sort()
        
        a = nums[0] * nums[1] * nums[-1]
        b = nums[-3] * nums[-2] * nums[-1]
        
        return a if a > b else b