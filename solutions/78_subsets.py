class Solution:
    
    def __init__(self):
        self.res = []
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self._backtracking(nums, [], 0)
        return self.res
    
    def _backtracking(self, nums, sub, idx):
        if idx == len(nums):
            self.res.append(sub)
            return 
        self._backtracking(nums, sub, idx + 1)
        self._backtracking(nums, sub + [nums[idx]], idx + 1)
