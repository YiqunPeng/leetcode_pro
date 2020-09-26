class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
    	"""Array.

    	Running time: O(n) where n is the length of nums.
    	"""
        res = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        return res
