class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    	"""Sort.

    	Running time: O(nlogn) where n == len(intervals).
    	"""
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        return res
