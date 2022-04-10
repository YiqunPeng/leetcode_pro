class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        res = []
        for i, gs in enumerate(groupSizes):
            d[gs].append(i)
            if len(d[gs]) == gs:
                res.append(d[gs])
                d[gs] = []
        return res
