class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Array.

        Running time: O(n) where n == len(intervals).
        """
        res = []
        p = 0
        while p < len(intervals) and intervals[p][0] < newInterval[0]:
            res.append(intervals[p])
            p += 1
        
        if res and newInterval[0] <= res[-1][1]:
            res[-1][1] = res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval)
        
        while p < len(intervals):
            if intervals[p][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[p][1])
            else:
                res.append(intervals[p])
            p += 1
        return res
