class Solution:
    
    def __init__(self):
        self.res = []
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Backtracking.

        Running time: O(n!) where n == len(nums).
        """
        nums.sort()
        self._backtracking(nums, set(), [])
        return self.res
    
    def _backtracking(self, nums, used, perm):
        if len(nums) == len(used):
            self.res.append(perm)
            return
        for i in range(len(nums)):
            if i in used or (i and i - 1 not in used and nums[i] == nums[i-1]):
                continue
            used.add(i)
            self._backtracking(nums, used, perm + [nums[i]])
            used.remove(i)
