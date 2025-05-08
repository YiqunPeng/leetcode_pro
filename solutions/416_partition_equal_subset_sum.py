class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        half_s = s // 2
        dp = [False] * (half_s + 1)
        dp[0] = True
        for n in nums:
            for i in range(half_s, 0, -1):
                if i - n >= 0:
                    dp[i] = dp[i] or dp[i - n]
                if dp[half_s]:
                    return True
        return False


class Solution2:

    def __init__(self):
        self.mem = dict()

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        return self._dfs(nums, 0, 0, s // 2)

    def _dfs(self, nums, idx, curr, half):
        if idx == len(nums):
            return curr == half
        if (idx, curr) in self.mem:
            return self.mem[(idx, curr)]
        p1 = self._dfs(nums, idx+1, curr+nums[idx], half)
        p2 = self._dfs(nums, idx+1, curr, half)
        self.mem[(idx, curr)] = p1 or p2
        return self.mem[(idx, curr)]