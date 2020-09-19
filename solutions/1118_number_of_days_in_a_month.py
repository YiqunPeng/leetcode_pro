class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        """Math.

        Running time: O(1).
        """
        month_days = {
            1: 31,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        
        if M in month_days:
            return month_days[M]
        
        if (Y % 4 != 0) or (Y % 100 == 0 and Y % 400 != 0):
            return 28
        else:
            return 29
