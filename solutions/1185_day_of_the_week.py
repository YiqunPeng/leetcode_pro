class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """Array.

        Running time: O(year + month).
        """
        week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        for y in range(1971, year):
            if self._is_leap_year(y):
                days += 366
            else:
                days += 365
        for m in range(1, month):
            days += month_days[m]
        if self._is_leap_year(year) and month > 2:
            days += 1
        days += day
        return week[(days-1) % 7]      
    
    def _is_leap_year(self, year):
        return (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)
