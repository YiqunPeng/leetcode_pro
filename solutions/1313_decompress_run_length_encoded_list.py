class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of nums.
    	"""
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i+1]] * nums[i])
        return res
