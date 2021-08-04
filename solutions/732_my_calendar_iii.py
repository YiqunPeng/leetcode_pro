class MyCalendarThree:

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> int:
        self._add(start, 's')
        self._add(end, 'e')
        res = 0
        k = 0
        for b in self.books:
            if b[1] == 's':
                k += 1
                res = max(res, k)
            else:
                k -= 1
        return res
    
    def _add(self, time, c):
        l, r = 0, len(self.books)
        while l < r:
            m = (l + r) // 2
            if self.books[m][0] < time or self.books[m][0] == time and c == 's':
                l = m + 1
            else:
                r = m
        self.books.insert(l, [time, c])
