class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pres = [0] * n
        pres[0] = nums[0]
        for i in range(1, n):
            pres[i] = pres[i-1] + nums[i]
        res = [0] * n
        for i in range(n):
            res[i] = nums[i] * (i + 1) - pres[i] + (pres[-1] - pres[i]) - (nums[i] * (n - (i + 1)))
        return res
