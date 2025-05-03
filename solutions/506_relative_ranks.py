class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = [(v, i) for i, v in enumerate(score)]
        s.sort(key=lambda x: x[0])
        res = [''] * len(s)
        rank = 1
        while s:
            v, i = s.pop()
            if rank == 1:
                res[i] = 'Gold Medal'
            elif rank == 2:
                res[i] = 'Silver Medal'
            elif rank == 3:
                res[i] = 'Bronze Medal'
            else:
                res[i] = str(rank)
            rank += 1
        return res
