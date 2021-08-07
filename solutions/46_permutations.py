class Solution:
    
    def __init__(self):
        self.res = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Backtracking.

        Running time: O(n!) where n == len(nums).
        """
        self._backtracking(nums, set(), [])
        return self.res
    
    def _backtracking(self, nums, used, perm):
        if len(used) == len(nums):
            self.res.append(perm)
            return
        for i in range(len(nums)):
            if i not in used:
                used.add(i)
                self._backtracking(nums, used, perm + [nums[i]])
                used.remove(i)
