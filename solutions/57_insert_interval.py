class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Array.

        Running time: O(n) where n == len(intervals).
        """
        n = len(intervals)
        l = 0
        while l < n and intervals[l][1] < newInterval[0]:
            l += 1
        r = n - 1
        while r >= 0 and intervals[r][0] > newInterval[1]:
            r -= 1
        if l <= r:
            newInterval[0] = min(newInterval[0], intervals[l][0])
            newInterval[1] = max(newInterval[1], intervals[r][1])
        intervals[l:r+1] = [newInterval]
        return intervals
