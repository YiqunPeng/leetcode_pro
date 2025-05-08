class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self._count_total_days(date1) - self._count_total_days(date2))

    def _count_total_days(self, date):
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10]) 
        days = 0
        for y in range(1971, year):
            if self._is_leap_year(y):
                days += 366
            else:
                days += 365
        for m in range(1, month):
            days += self._days_in_month(year, m)
        return days + day

    def _is_leap_year(self, y):
        return y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)    
    
    def _days_in_month(self, y, m):
        if m in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif m in (4, 6, 9, 11):
            return 30
        else:
            if self._is_leap_year(y):
                return 29
            return 28