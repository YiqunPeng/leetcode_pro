class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
    	"""Array.

    	Running time: O(n) where n is the length of nums.
    	"""
        p = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if p is None or i - p > k:
                    p = i
                else:
                    return False
        return True
