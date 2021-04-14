class Solution:
    
    def __init__(self):
        self.res = set()
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            self._dfs(nums, i, [nums[i]])
        return [list(i) for i in self.res]
    
    def _dfs(self, nums, last, sub):
        if len(sub) >= 2:
            self.res.add(tuple(sub))
        for i in range(last+1, len(nums)):
            if nums[i] >= nums[last]:
                self._dfs(nums, i, sub + [nums[i]])
