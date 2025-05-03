class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = -1
        j = len(nums) - 1
        for i in range(len(nums)):
            while i < j and nums[i] + nums[j] >= k:
                j -= 1            
            if i < j:
                res = max(res, nums[i] + nums[j])
        return res