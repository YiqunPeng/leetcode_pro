class Solution:
    
    def __init__(self):
        self.mem = {}
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self._dfs(nums, 0, 0, target)
    
    def _dfs(self, nums, pos, s, t):
        if pos == len(nums):
            if s == t:
                return 1
            else:
                return 0
        if (pos, s) in self.mem:
            return self.mem[(pos, s)]
        res = self._dfs(nums, pos + 1, s + nums[pos], t) + self._dfs(nums, pos + 1, s - nums[pos], t)
        self.mem[(pos, s)] = res
        return res
