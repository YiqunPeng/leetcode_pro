class Solution:
    
    def __init__(self):
        self.flat = []
        self.maxd = 0
    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self._dfs(nestedList, 0)
        res = 0
        for d, v in self.flat:
            res += (self.maxd + 1 - d) * v
        return res
            
        
    def _dfs(self, nestedList, d):
        self.maxd = max(self.maxd, d)
        for item in nestedList:
            if item.isInteger():
                self.flat.append((d, item.getInteger()))
            else:
                self._dfs(item.getList(), d + 1)
