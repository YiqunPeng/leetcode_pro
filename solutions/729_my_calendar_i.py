class MyCalendar:

    def __init__(self):
        self.bookings = [[-1, 0], [10**9, 10**9+1]]

    def book(self, start: int, end: int) -> bool:
        """Binary search.

        Running time: O(logn + n) where n is the length of self.bookings.
        """
        i = self._search(start)
        if self.bookings[i-1][1] <= start < end <= self.bookings[i][0]:
            self.bookings.insert(i, [start, end])
            return True
        return False 
            
    def _search(self, s):
        l, r = 0, len(self.bookings)
        while l < r:
            m = (r + l) // 2
            if self.bookings[m][0] < s:
                l = m + 1
            else:
                r = m
        return r
