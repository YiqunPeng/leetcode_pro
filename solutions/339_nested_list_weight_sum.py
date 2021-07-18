class Solution:
    
    def __init__(self):
        self.s = 0
    
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self._recursion(nestedList, 1)
        return self.s
    
    def _recursion(self, nestedList, depth):
        for item in nestedList:
            if item.isInteger():
                self.s += item.getInteger() * depth
            else:
                self._recursion(item.getList(), depth + 1)
