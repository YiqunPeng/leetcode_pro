class Solution:
    
    def __init__(self):
        self.res = []
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self._backtracking(nums, [], 0)
        return self.res
    
    def _backtracking(self, nums, sub, idx):
        self.res.append(sub)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self._backtracking(nums, sub + [nums[i]], i + 1)
