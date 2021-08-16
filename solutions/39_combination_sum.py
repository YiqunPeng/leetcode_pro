class Solution:
    
    def __init__(self):
        self.res = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self._backtracking(candidates, 0, 0, [], target)
        return self.res
    
    def _backtracking(self, c, idx, s, comb, t):
        if s == t:
            self.res.append(comb)
            return
        for i in range(idx, len(c)):
            if s + c[i] > t:
                break
            self._backtracking(c, i, s + c[i], comb + [c[i]], t)
