class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    	"""Sort.

    	Running time: O(nlogn) where n == len(intervals).
    	"""
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in intervals:
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res
