class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n
        m = nums[0]
        for i in range(1, n):
            m = min(m, nums[i-1])
            left[i] = m
        m = nums[-1]
        for i in range(n-2, -1, -1):
            m = min(m, nums[i+1])
            right[i] = m
        
        res = 4 * 10 ** 8
        for i in range(1, n - 1):
            if left[i] < nums[i] and right[i] < nums[i]:
                res = min(res, left[i] + nums[i] + right[i])
        return -1 if res == 4 * 10 ** 8 else res