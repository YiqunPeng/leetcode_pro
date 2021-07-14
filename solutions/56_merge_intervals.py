class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    	"""Sort.

    	Running time: O(nlogn) where n == len(intervals).
    	"""
        intervals.sort(key=lambda x:x[0])
        l, r = 0, 1
        while r < len(intervals):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
            else:
                l += 1
                intervals[l] = intervals[r]
            r += 1
        return intervals[:l+1]
