class Solution:
    
    def __init__(self):
        self.res = 0
    
    def countArrangement(self, n: int) -> int:
        nums = set(list(range(1, n + 1)))
        self._dfs(1, nums)
        return self.res
    
    def _dfs(self, i, nums):
        if not nums:
            self.res += 1
            return 
        for num in list(nums):
            if i % num == 0 or num % i == 0:
                nums.remove(num)
                self._dfs(i + 1, nums)
                nums.add(num)
