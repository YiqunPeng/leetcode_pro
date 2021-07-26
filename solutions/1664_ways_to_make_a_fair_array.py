class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        left = [0, 0]
        right = [sum(nums[::2]), sum(nums[1::2])]
        res = 0
        for i in range(len(nums)):
            right[i%2] -= nums[i]
            if right[0] + left[1] == right[1] + left[0]:
                res += 1
            left[i%2] += nums[i]
        return res
