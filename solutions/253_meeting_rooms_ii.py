class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Sort.

        Running time: O(nlogn) where n == len(intervals).
        """
        t = []
        for s, e in intervals:
            t.append((s, 1))
            t.append((e, -1))
        t.sort(key=lambda x: (x[0], x[1]))
        res = 0
        room = 0
        for _, i in t:
            room += i
            res = max(res, room)
        return res
