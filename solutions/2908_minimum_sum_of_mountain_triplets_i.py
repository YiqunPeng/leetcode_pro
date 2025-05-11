class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = 200
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[j] <= nums[i]:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[k] < nums[j]:
                        res = min(res, nums[i] + nums[j] + nums[k])
        return -1 if res == 200 else res