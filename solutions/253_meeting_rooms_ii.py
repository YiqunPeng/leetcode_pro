class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Sort.

        Running time: O(nlogn) where n == len(intervals).
        """
        timestamps = []
        for s, e in intervals:
            timestamps.append((s, 's'))
            timestamps.append((e, 'e'))
        timestamps.sort()
        res = 0
        rooms = 0
        for t, c in timestamps:
            if c == 's':
                rooms += 1
            else:
                rooms -= 1
            res = max(res, rooms)
        return res
