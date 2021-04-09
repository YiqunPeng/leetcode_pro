class Solution:
    def depthSum(self, nestedList: List[NestedInteger], d=1) -> int:
        res = 0
        for item in nestedList:
            if item.isInteger():
                res += item.getInteger() * d
            else:
                res += self.depthSum(item.getList(), d + 1)
        return res
