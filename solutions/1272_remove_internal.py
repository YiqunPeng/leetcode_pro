class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for a, b in intervals:
            if a < toBeRemoved[0]:
                res.append([a, min(toBeRemoved[0], b)])
            if b > toBeRemoved[1]:
                res.append([max(a, toBeRemoved[1]), b])
        return res
