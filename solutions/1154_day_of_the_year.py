class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        splits = date.split('-')
        year, month, day = int(splits[0]), int(splits[1]), int(splits[2])
        leap = 0
        if month > 2 and self._is_leap_year(year):
            leap = 1
        res = 0
        for m in range(1, month):
            res += month_days[m]
        return res + day + leap
    
    def _is_leap_year(self, year):
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
