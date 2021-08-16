class Solution:
    
    def __init__(self):
        self.res = []
        self.n = 0
        self.k = 0
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self._backtracking(1, 0, [])
        return self.res
    
    def _backtracking(self, idx, s, comb):
        if len(comb) == self.k:
            if s == self.n:
                self.res.append(comb)
            return
        for i in range(idx, 10):
            if s + i > self.n:
                break
            self._backtracking(i + 1, s + i, comb + [i])
