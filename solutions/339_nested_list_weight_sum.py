class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        s = 0
        if not nestedList:
            return s
        q = deque([(i, 1) for i in nestedList])
        while q:
            l, d = q.popleft()
            if l.isInteger():
                s += l.getInteger() * d
            else:
                for i in l.getList():
                    q.append((i, d + 1))
        return s
