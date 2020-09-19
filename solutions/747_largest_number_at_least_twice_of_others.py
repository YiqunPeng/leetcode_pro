class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """Two pointers.

        Running time: O(n) where n is the length of nums.
        """
        if not nums:
            return -1
        
        max_v, max_p = nums[0], 0
        smax_v = None
        
        for i in range(1, len(nums)):
            if nums[i] >= max_v:
                smax_v = max_v
                max_v = nums[i]
                max_p = i
            elif smax_v is None or nums[i] > smax_v:
                smax_v = nums[i]
        
        if smax_v is None or max_v >= smax_v * 2:
            return max_p
        else:
            return -1