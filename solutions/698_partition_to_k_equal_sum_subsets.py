class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        nums.sort()
        if s % k != 0:
            return False
        dsum = s // k
        return self._dfs(nums, dsum, k, 1, 0, [False] * len(nums), 0)
    
    def _dfs(self, nums, dsum, k, g, gsum, used, idx):
        if g == k + 1:
            return True
        for i in range(idx, len(nums)):
            if not used[i]:
                if gsum + nums[i] == dsum:
                    used[i] = True
                    if self._dfs(nums, dsum, k, g + 1, 0, used, 0):
                        return True
                    used[i] = False
                elif gsum + nums[i] < dsum:
                    used[i] = True
                    if self._dfs(nums, dsum, k, g, gsum + nums[i], used, i + 1):
                        return True
                    used[i] = False
        return False
