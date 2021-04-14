class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ops += [[m, n]]
        return min(o[0] for o in ops) * min(o[1] for o in ops)
